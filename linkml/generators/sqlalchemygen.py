from __future__ import annotations

import logging
import os
from collections import defaultdict
from dataclasses import dataclass
from types import ModuleType

import click
from jinja2 import Template
from linkml_runtime.linkml_model import Annotation, ClassDefinition, ClassDefinitionName, SchemaDefinition
from linkml_runtime.utils.compile_python import compile_python
from linkml_runtime.utils.formatutils import camelcase, underscore
from linkml_runtime.utils.schemaview import SchemaView
from sqlalchemy import Enum

from linkml._version import __version__
from linkml.generators.pydanticgen import PydanticGenerator
from linkml.generators.pythongen import PythonGenerator
from linkml.generators.sqlalchemy.sqlalchemy_declarative_template import sqlalchemy_declarative_template_str
from linkml.generators.sqlalchemy.sqlalchemy_imperative_template import sqlalchemy_imperative_template_str
from linkml.generators.sqltablegen import SQLTableGenerator
from linkml.transformers.relmodel_transformer import ForeignKeyPolicy, RelationalModelTransformer
from linkml.utils.generator import Generator, shared_arguments

logger = logging.getLogger(__name__)


class TemplateEnum(Enum):
    DECLARATIVE = "declarative"
    IMPERATIVE = "imperative"


@dataclass
class SQLAlchemyGenerator(Generator):
    """
    Generates SQL Alchemy classes

    See also: :class:`~linkml.generators.sqltablegen.SQLTableGenerator`
    """

    # ClassVars
    generatorname = os.path.basename(__file__)
    generatorversion = "0.1.1"
    valid_formats = ["sqla"]
    file_extension = "py"
    uses_schemaloader = False
    template: TemplateEnum | None = None

    # ObjectVars
    original_schema: SchemaDefinition | str = None

    def __post_init__(self) -> None:
        self.original_schema = self.schema
        self.schemaview = SchemaView(self.schema)
        super().__post_init__()

    def generate_sqla(
        self,
        model_path: str | None = None,
        no_model_import: bool = False,
        template: TemplateEnum | None = None,
        foreign_key_policy: ForeignKeyPolicy | None = None,
        **kwargs,
    ) -> str:
        template = template or self.template or TemplateEnum.IMPERATIVE
        sqltr = RelationalModelTransformer(self.schemaview)
        if foreign_key_policy:
            sqltr.foreign_key_policy = foreign_key_policy
        tgen = SQLTableGenerator(self.schemaview.schema)
        tr_result = sqltr.transform(**kwargs)
        tr_schema = tr_result.schema
        for c in tr_schema.classes.values():
            for a in c.attributes.values():
                sql_range = tgen.get_sql_range(a, tr_schema)
                sql_type = sql_range.__repr__()
                ann = Annotation("sql_type", sql_type)
                a.annotations[ann.tag] = ann
        if template == TemplateEnum.IMPERATIVE:
            template_str = sqlalchemy_imperative_template_str
        elif template == TemplateEnum.DECLARATIVE:
            template_str = sqlalchemy_declarative_template_str
        else:
            raise Exception(f"Unknown template type: {template}")
        template_obj = Template(template_str)
        if model_path is None:
            model_path = self.schema.name
        logger.info(f"Package for dataclasses ==  {model_path}")
        backrefs = defaultdict(list)
        for m in tr_result.mappings:
            backrefs[m.source_class].append(m)
        self.add_safe_aliases(tr_schema)
        tr_sv = SchemaView(tr_schema)
        rel_schema_classes_ordered = [tr_sv.get_class(cn, strict=True) for cn in self.order_classes_by_hierarchy(tr_sv)]
        rel_schema_classes_ordered = [c for c in rel_schema_classes_ordered if not self.skip(c)]
        for c in rel_schema_classes_ordered:
            # For SQLA there needs to be a primary key for each class;
            # autogenerate this as a compound key if none declared
            has_pk = any(a for a in c.attributes.values() if "primary_key" in a.annotations)
            if not has_pk:
                for a in c.attributes.values():
                    ann = Annotation("primary_key", "true")
                    a.annotations[ann.tag] = ann
        code = template_obj.render(
            model_path=model_path,
            mappings=tr_result.mappings,
            backrefs=backrefs,
            classname=camelcase,
            no_model_import=no_model_import,
            is_join_table=lambda c: any(tag for tag in c.annotations.keys() if tag == "linkml:derived_from"),
            classes=rel_schema_classes_ordered,
        )
        logger.debug(f"# Generated code:\n{code}")
        return code

    def serialize(self, **kwargs) -> str:
        return self.generate_sqla(**kwargs)

    def compile_sqla(
        self,
        compile_python_dataclasses=False,
        pydantic=False,
        model_path=None,
        template: TemplateEnum = TemplateEnum.IMPERATIVE,
        **kwargs,
    ) -> ModuleType:
        """
        Generates and compiles SQL Alchemy bindings

        - If template is DECLARATIVE, then a single python module with classes is generated
        - If template is IMPERATIVE, only mappings are generated
             - if compile_python_dataclasses is True then a standard datamodel is generated

        :param compile_python_dataclasses: (default False)
        :param pydantic:
        :param model_path:
        :param template:
        :param kwargs:
        :return:
        """

        if model_path is None:
            model_path = self.schema.name

        if template == TemplateEnum.DECLARATIVE:
            sqla_code = self.generate_sqla(model_path=None, no_model_import=True, template=template, **kwargs)
            return compile_python(sqla_code, package_path=model_path)
        elif compile_python_dataclasses:
            # concatenate the python dataclasses with the sqla code
            if pydantic:
                # mixin inheritance doesn't get along with SQLAlchemy's imperative (aka classical) mapping
                pygen = PydanticGenerator(self.original_schema, extra_fields="allow", gen_mixin_inheritance=False)
            else:
                pygen = PythonGenerator(self.original_schema)
            dc_code = pygen.serialize()
            sqla_code = self.generate_sqla(model_path=None, no_model_import=True, **kwargs)
            return compile_python(f"{dc_code}\n{sqla_code}", package_path=model_path)
        else:
            code = self.generate_sqla(model_path=model_path, **kwargs)
            return compile_python(code, package_path=model_path)

    @staticmethod
    def add_safe_aliases(schema: SchemaDefinition) -> None:
        for c in schema.classes.values():
            for a in c.attributes.values():
                a.alias = underscore(a.name)

    @staticmethod
    def skip(cls: ClassDefinition) -> bool:
        is_skip = len(cls.attributes) == 0
        if is_skip:
            logger.error(f"SKIPPING: {cls.name}")
        return is_skip

    # TODO: move this
    @staticmethod
    def order_classes_by_hierarchy(sv: SchemaView) -> list[ClassDefinitionName]:
        olist = sv.class_roots()
        unprocessed = [cn for cn in sv.all_classes() if cn not in olist]
        while len(unprocessed) > 0:
            ext_list = [cn for cn in unprocessed if not any(p for p in sv.class_parents(cn) if p not in olist)]
            if len(ext_list) == 0:
                raise ValueError(f"Cycle in hierarchy, cannot process: {unprocessed}")
            olist += ext_list
            unprocessed = [cn for cn in unprocessed if cn not in olist]
        return olist


@shared_arguments(SQLAlchemyGenerator)
@click.option(
    "--declarative/--no-declarative",
    default=True,
    show_default=True,
    help="Generate SQL Alchemy declarative vs imperative",
)
@click.option(
    "--generate-classes/--no-generate-classes",
    default=False,
    show_default=True,
    help="If True, generate Python datamodel (imperative mode only)",
)
@click.option(
    "--pydantic/--no-pydantic",
    default=False,
    show_default=True,
    help="If True, generate Pydantic classes (imperative mode only)",
)
@click.option(
    "--use-foreign-keys/--no-use-foreign-keys",
    default=True,
    show_default=True,
    help="Emit FK declarations",
)
@click.version_option(__version__, "-V", "--version")
@click.command(name="sqla")
def cli(yamlfile, declarative, generate_classes, pydantic, use_foreign_keys=True, **args):
    """Generate SQL DDL representation"""
    if pydantic:
        pygen = PydanticGenerator(yamlfile)
        print(pygen.serialize())
    gen = SQLAlchemyGenerator(yamlfile, **args)
    if declarative:
        t = TemplateEnum.DECLARATIVE
    else:
        t = TemplateEnum.IMPERATIVE
    if use_foreign_keys:
        foreign_key_policy = None  # default
    else:
        foreign_key_policy = ForeignKeyPolicy.NO_FOREIGN_KEYS
    print(gen.generate_sqla(template=t, foreign_key_policy=foreign_key_policy))
    if generate_classes:
        raise NotImplementedError("generate classes not implemented")


if __name__ == "__main__":
    cli()
