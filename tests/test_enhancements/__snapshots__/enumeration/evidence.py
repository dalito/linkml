# Auto generated from evidence.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: evidence
#
# id: http://example.org/test/evidence
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Namespaces
CLUE = CurieNamespace('CLUE', 'http://example.org/clue/')
EVIDENCE = CurieNamespace('evidence', 'http://example.org/test/evidence/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = EVIDENCE


# Types

# Class references
class EvidencerName(extended_str):
    pass


@dataclass(repr=False)
class Evidencer(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EVIDENCE["Evidencer"]
    class_class_curie: ClassVar[str] = "evidence:Evidencer"
    class_name: ClassVar[str] = "evidencer"
    class_model_uri: ClassVar[URIRef] = EVIDENCE.Evidencer

    name: Union[str, EvidencerName] = None
    code: Union[str, "Evidence"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, EvidencerName):
            self.name = EvidencerName(self.name)

        if self._is_empty(self.code):
            self.MissingRequiredField("code")
        if not isinstance(self.code, Evidence):
            self.code = Evidence(self.code)

        super().__post_init__(**kwargs)


# Enumerations
class Evidence(EnumDefinitionImpl):
    """
    Permissible values for CLUE evidence fragments
    """
    IEA = PermissibleValue(
        text="IEA",
        description="Colonel Mustard in the Ballroom")
    ISS = PermissibleValue(
        text="ISS",
        description="Mrs. Peacock with the Dagger",
        meaning=CLUE["1173"])

    _defn = EnumDefinition(
        name="Evidence",
        description="Permissible values for CLUE evidence fragments",
        code_set=CLUE["fragment_vd"],
    )

# Slots
class slots:
    pass

slots.evidencer__name = Slot(uri=EVIDENCE.name, name="evidencer__name", curie=EVIDENCE.curie('name'),
                   model_uri=EVIDENCE.evidencer__name, domain=None, range=URIRef)

slots.evidencer__code = Slot(uri=EVIDENCE.code, name="evidencer__code", curie=EVIDENCE.curie('code'),
                   model_uri=EVIDENCE.evidencer__code, domain=None, range=Union[str, "Evidence"])
