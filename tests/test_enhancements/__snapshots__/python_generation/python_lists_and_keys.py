# Auto generated from python_lists_and_keys.yaml by pythongen.py version: 0.0.1
# Generation date: 2000-01-01T00:00:00
# Schema: lists_and_keys
#
# id: http://examples.org/linkml/test/lists_and_keys
# description: python generation for variants of lists and keys
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

from . python_complex_ranges import IdentifiedOneElementClass, IdentifiedOneElementClassName, IdentifiedThreeElementClass, IdentifiedThreeElementClassName, KeyedOneElementClass, KeyedOneElementClassName, KeyedThreeElementClass, KeyedThreeElementClassName, KeyedTwoElementClass, KeyedTwoElementClassName, OneElementClass, ThreeElementClass, TwoElementClass

metamodel_version = "1.7.0"
version = None

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LISTS_AND_KEYS = CurieNamespace('lists_and_keys', 'http://examples.org/linkml/test/lists_and_keys')
DEFAULT_ = LISTS_AND_KEYS


# Types

# Class references



@dataclass(repr=False)
class OptionalOneElementRange(YAMLRoot):
    """
    Range is a optional class that contains one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalOneElementRange"
    class_name: ClassVar[str] = "OptionalOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalOneElementRange

    v1: Optional[Union[dict, OneElementClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, OneElementClass):
            self.v1 = OneElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredOneElementRange(YAMLRoot):
    """
    Range is a required class that contains one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredOneElementRange"
    class_name: ClassVar[str] = "RequiredOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredOneElementRange

    v1: Union[dict, OneElementClass] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, OneElementClass):
            self.v1 = OneElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalOneElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contain one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalOneElementRangeList"
    class_name: ClassVar[str] = "OptionalOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalOneElementRangeList

    v1: Optional[Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, OneElementClass) else OneElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredOneElementRangeList(OptionalOneElementRangeList):
    """
    Range is a required list of a class that contain one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredOneElementRangeList"
    class_name: ClassVar[str] = "RequiredOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredOneElementRangeList

    v1: Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, OneElementClass) else OneElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredTwoElementRangeList(YAMLRoot):
    """
    Range is a required list of a class that contain two non-key/non-identifier elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredTwoElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredTwoElementRangeList"
    class_name: ClassVar[str] = "RequiredTwoElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredTwoElementRangeList

    v1: Union[Union[dict, TwoElementClass], list[Union[dict, TwoElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, TwoElementClass) else TwoElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredThreeElementRangeList(YAMLRoot):
    """
    Range is a required list of a class that contain two non-key/non-identifier elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredThreeElementRangeList

    v1: Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, ThreeElementClass) else ThreeElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedOneElementRange(YAMLRoot):
    """
    Range is a optional class that contains one key element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedOneElementRange"
    class_name: ClassVar[str] = "OptionalKeyedOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedOneElementRange

    v1: Optional[Union[str, KeyedOneElementClassName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, KeyedOneElementClassName):
            self.v1 = KeyedOneElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedOneElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one key element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedOneElementRangeList"
    class_name: ClassVar[str] = "OptionalKeyedOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedOneElementRangeList

    v1: Optional[Union[Union[str, KeyedOneElementClassName], list[Union[str, KeyedOneElementClassName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, KeyedOneElementClassName) else KeyedOneElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalIdentifiedOneElementRange(YAMLRoot):
    """
    Range is a optional class that contains one identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalIdentifiedOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalIdentifiedOneElementRange"
    class_name: ClassVar[str] = "OptionalIdentifiedOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalIdentifiedOneElementRange

    v1: Optional[Union[str, IdentifiedOneElementClassName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, IdentifiedOneElementClassName):
            self.v1 = IdentifiedOneElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalIdentifiedOneElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalIdentifiedOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalIdentifiedOneElementRangeList"
    class_name: ClassVar[str] = "OptionalIdentifiedOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalIdentifiedOneElementRangeList

    v1: Optional[Union[Union[str, IdentifiedOneElementClassName], list[Union[str, IdentifiedOneElementClassName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, IdentifiedOneElementClassName) else IdentifiedOneElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedTwoElementRange(YAMLRoot):
    """
    Range is a optional class that contains one key and one regular element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedTwoElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedTwoElementRange"
    class_name: ClassVar[str] = "OptionalKeyedTwoElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedTwoElementRange

    v1: Optional[Union[str, KeyedTwoElementClassName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, KeyedTwoElementClassName):
            self.v1 = KeyedTwoElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedTwoElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one key and one regular element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedTwoElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedTwoElementRangeList"
    class_name: ClassVar[str] = "OptionalKeyedTwoElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedTwoElementRangeList

    v1: Optional[Union[Union[str, KeyedTwoElementClassName], list[Union[str, KeyedTwoElementClassName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, KeyedTwoElementClassName) else KeyedTwoElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedThreeElementRange(YAMLRoot):
    """
    Range is a optional class that contains one key and two regular elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedThreeElementRange"
    class_name: ClassVar[str] = "OptionalKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedThreeElementRange

    v1: Optional[Union[str, KeyedThreeElementClassName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, KeyedThreeElementClassName):
            self.v1 = KeyedThreeElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalKeyedThreeElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one key and two regular elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalKeyedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalKeyedThreeElementRangeList"
    class_name: ClassVar[str] = "OptionalKeyedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalKeyedThreeElementRangeList

    v1: Optional[Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, KeyedThreeElementClassName) else KeyedThreeElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredIdentifiedThreeElementRange(YAMLRoot):
    """
    Range is a required class that contains one identifier and two regular elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "RequiredIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredIdentifiedThreeElementRange

    v1: Union[str, IdentifiedThreeElementClassName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, IdentifiedThreeElementClassName):
            self.v1 = IdentifiedThreeElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredIdentifiedThreeElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one identifier and two regular elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredIdentifiedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredIdentifiedThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredIdentifiedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredIdentifiedThreeElementRangeList

    v1: Union[Union[str, IdentifiedThreeElementClassName], list[Union[str, IdentifiedThreeElementClassName]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, IdentifiedThreeElementClassName) else IdentifiedThreeElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredKeyedThreeElementRangeList(YAMLRoot):
    """
    Range is a optional list of a class that contains one key and two regular elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredKeyedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredKeyedThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredKeyedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredKeyedThreeElementRangeList

    v1: Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, KeyedThreeElementClassName) else KeyedThreeElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedOneElementRange(RequiredOneElementRange):
    """
    Range is a required inlined class that contains one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedOneElementRange"
    class_name: ClassVar[str] = "RequiredInlinedOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedOneElementRange

    v1: Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, OneElementClass) else OneElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedOneElementRangeList(RequiredOneElementRangeList):
    """
    Range is a required inlined list of a class that contains one non-key/non-identifier element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedOneElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedOneElementRangeList

    v1: Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, OneElementClass) else OneElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedTwoElementRangeList(RequiredTwoElementRangeList):
    """
    Range is a required inlined list of a class that contains two non-key/non-identifier elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedTwoElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedTwoElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedTwoElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedTwoElementRangeList

    v1: Union[Union[dict, TwoElementClass], list[Union[dict, TwoElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, TwoElementClass) else TwoElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedThreeElementRangeList(RequiredThreeElementRangeList):
    """
    Range is a required inlined list of a class that contains two non-key/non-identifier elements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedThreeElementRangeList

    v1: Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, ThreeElementClass) else ThreeElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedOneElementRange(OptionalKeyedOneElementRange):
    """
    Range is an inlined required class that contains one key element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedOneElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedOneElementRange"
    class_name: ClassVar[str] = "RequiredInlinedKeyedOneElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedOneElementRange

    v1: Union[list[Union[str, KeyedOneElementClassName]], dict[Union[str, KeyedOneElementClassName], Union[dict, KeyedOneElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedOneElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedOneElementRangeList(OptionalKeyedOneElementRangeList):
    """
    Range is an inlined required list of a class that contains one key element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedOneElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedKeyedOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedOneElementRangeList

    v1: Union[list[Union[str, KeyedOneElementClassName]], dict[Union[str, KeyedOneElementClassName], Union[dict, KeyedOneElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedOneElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedTwoElementRange(OptionalKeyedTwoElementRange):
    """
    Range is an inlined required class that contains one key element and one non-key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedTwoElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedTwoElementRange"
    class_name: ClassVar[str] = "RequiredInlinedKeyedTwoElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedTwoElementRange

    v1: Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedTwoElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedTwoElementRangeList(OptionalKeyedTwoElementRangeList):
    """
    Range is an inlined required list of a class that contains one key element and  one non-key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedTwoElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedTwoElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedKeyedTwoElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedTwoElementRangeList

    v1: Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedTwoElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedThreeElementRange(OptionalKeyedThreeElementRange):
    """
    Range is an inlined required class that contains one key element and two non-keys
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedThreeElementRange"
    class_name: ClassVar[str] = "RequiredInlinedKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedThreeElementRange

    v1: Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedKeyedThreeElementRangeList(OptionalKeyedThreeElementRangeList):
    """
    Range is an inlined required list of a class that contains one key element and two non-keys
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedKeyedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedKeyedThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedKeyedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedKeyedThreeElementRangeList

    v1: Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedIdentifiedOneElementRangeList(YAMLRoot):
    """
    Range is an inlined required list of a class that contains one identified element
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedIdentifiedOneElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedIdentifiedOneElementRangeList"
    class_name: ClassVar[str] = "RequiredInlinedIdentifiedOneElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedIdentifiedOneElementRangeList

    v1: Union[list[Union[str, IdentifiedOneElementClassName]], dict[Union[str, IdentifiedOneElementClassName], Union[dict, IdentifiedOneElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=IdentifiedOneElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EntryList(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["EntryList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:EntryList"
    class_name: ClassVar[str] = "EntryList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.EntryList

    entries: Optional[Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=KeyedTwoElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalThreeElementRange(YAMLRoot):
    """
    Case 1.1(o) -- single values optional slot - range has no keys or identifiers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalThreeElementRange"
    class_name: ClassVar[str] = "OptionalThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalThreeElementRange

    v1: Optional[Union[dict, ThreeElementClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, ThreeElementClass):
            self.v1 = ThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredThreeElementRange(YAMLRoot):
    """
    Case 1.1(r) -- single values optional slot - range has no keys or identifiers
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredThreeElementRange"
    class_name: ClassVar[str] = "RequiredThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredThreeElementRange

    v1: Union[dict, ThreeElementClass] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, ThreeElementClass):
            self.v1 = ThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalIdentifiedThreeElementRange(YAMLRoot):
    """
    Case 1.2(o) -- single values optional slot - range has an identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "OptionalIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalIdentifiedThreeElementRange

    v1: Optional[Union[str, IdentifiedThreeElementClassName]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, IdentifiedThreeElementClassName):
            self.v1 = IdentifiedThreeElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredKeyedThreeElementRange(YAMLRoot):
    """
    Case 1.2(r) -- single values optional slot - range has a key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredKeyedThreeElementRange"
    class_name: ClassVar[str] = "RequiredKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredKeyedThreeElementRange

    v1: Union[str, KeyedThreeElementClassName] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, KeyedThreeElementClassName):
            self.v1 = KeyedThreeElementClassName(self.v1)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalInlinedKeyedThreeElementRange(YAMLRoot):
    """
    Case 1.3(o) -- single values optional slot - range has an identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalInlinedKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalInlinedKeyedThreeElementRange"
    class_name: ClassVar[str] = "OptionalInlinedKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalInlinedKeyedThreeElementRange

    v1: Optional[Union[dict, KeyedThreeElementClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, KeyedThreeElementClass):
            self.v1 = KeyedThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedIdentifiedThreeElementRange(YAMLRoot):
    """
    Case 1.3(r) -- single values optional slot - range has a key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "RequiredInlinedIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedIdentifiedThreeElementRange

    v1: Union[dict, IdentifiedThreeElementClass] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, IdentifiedThreeElementClass):
            self.v1 = IdentifiedThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalInlinedAsListKeyedThreeElementRange(YAMLRoot):
    """
    Case 1.4(o) -- single values optional slot - range has an identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalInlinedAsListKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalInlinedAsListKeyedThreeElementRange"
    class_name: ClassVar[str] = "OptionalInlinedAsListKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalInlinedAsListKeyedThreeElementRange

    v1: Optional[Union[dict, KeyedThreeElementClass]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.v1 is not None and not isinstance(self.v1, KeyedThreeElementClass):
            self.v1 = KeyedThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredInlinedAsListIdentifiedThreeElementRange(YAMLRoot):
    """
    Case 1.4(r) -- single values optional slot - range has a key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredInlinedAsListIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredInlinedAsListIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "RequiredInlinedAsListIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredInlinedAsListIdentifiedThreeElementRange

    v1: Union[dict, IdentifiedThreeElementClass] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, IdentifiedThreeElementClass):
            self.v1 = IdentifiedThreeElementClass(**as_dict(self.v1))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalMultivaluedThreeElementRange(YAMLRoot):
    """
    Case 2.1(o) -- multivalued optional slot - range has no key or identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalMultivaluedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalMultivaluedThreeElementRange"
    class_name: ClassVar[str] = "OptionalMultivaluedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalMultivaluedThreeElementRange

    v1: Optional[Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, ThreeElementClass) else ThreeElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredMultivaluedThreeElementRange(YAMLRoot):
    """
    Case 2.1(r) -- multivalued optional slot - range has no key or identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredMultivaluedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredMultivaluedThreeElementRange"
    class_name: ClassVar[str] = "RequiredMultivaluedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredMultivaluedThreeElementRange

    v1: Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, ThreeElementClass) else ThreeElementClass(**as_dict(v)) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalMultivaluedKeyedThreeElementRange(YAMLRoot):
    """
    Case 2.2(o) -- multivalued optional slot - range has a key
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalMultivaluedKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalMultivaluedKeyedThreeElementRange"
    class_name: ClassVar[str] = "OptionalMultivaluedKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalMultivaluedKeyedThreeElementRange

    v1: Optional[Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, KeyedThreeElementClassName) else KeyedThreeElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredMultivaluedIdentifiedThreeElementRange(YAMLRoot):
    """
    Case 2.2(r) -- multivalued required slot - range has an identifier
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredMultivaluedIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredMultivaluedIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "RequiredMultivaluedIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredMultivaluedIdentifiedThreeElementRange

    v1: Union[Union[str, IdentifiedThreeElementClassName], list[Union[str, IdentifiedThreeElementClassName]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        if not isinstance(self.v1, list):
            self.v1 = [self.v1] if self.v1 is not None else []
        self.v1 = [v if isinstance(v, IdentifiedThreeElementClassName) else IdentifiedThreeElementClassName(v) for v in self.v1]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalMultivaluedInlinedListIdentifiedThreeElementRange(YAMLRoot):
    """
    2.3(o) Range is an optional identified three element class that is represented as an inlined list
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalMultivaluedInlinedListIdentifiedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalMultivaluedInlinedListIdentifiedThreeElementRange"
    class_name: ClassVar[str] = "OptionalMultivaluedInlinedListIdentifiedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalMultivaluedInlinedListIdentifiedThreeElementRange

    v1: Optional[Union[dict[Union[str, IdentifiedThreeElementClassName], Union[dict, IdentifiedThreeElementClass]], list[Union[dict, IdentifiedThreeElementClass]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="v1", slot_type=IdentifiedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredMultivaluedInlinedListKeyedThreeElementRangeList(YAMLRoot):
    """
    2.3(r) Range is a required keyed three element class that is represented as an inlined list
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredMultivaluedInlinedListKeyedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredMultivaluedInlinedListKeyedThreeElementRangeList"
    class_name: ClassVar[str] = "RequiredMultivaluedInlinedListKeyedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredMultivaluedInlinedListKeyedThreeElementRangeList

    v1: Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_list(slot_name="v1", slot_type=KeyedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OptionalMultivaluedInlinedIdentifiedThreeElementRangeList(YAMLRoot):
    """
    2.4(o) Range is an optional identified three element class that is represented as an inlined dictionary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["OptionalMultivaluedInlinedIdentifiedThreeElementRangeList"]
    class_class_curie: ClassVar[str] = "lists_and_keys:OptionalMultivaluedInlinedIdentifiedThreeElementRangeList"
    class_name: ClassVar[str] = "OptionalMultivaluedInlinedIdentifiedThreeElementRangeList"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.OptionalMultivaluedInlinedIdentifiedThreeElementRangeList

    v1: Optional[Union[dict[Union[str, IdentifiedThreeElementClassName], Union[dict, IdentifiedThreeElementClass]], list[Union[dict, IdentifiedThreeElementClass]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=IdentifiedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RequiredMultivaluedInlinedKeyedThreeElementRange(YAMLRoot):
    """
    2.4(r) Range is a required keyed three element class that is represented as an inlined dictionary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LISTS_AND_KEYS["RequiredMultivaluedInlinedKeyedThreeElementRange"]
    class_class_curie: ClassVar[str] = "lists_and_keys:RequiredMultivaluedInlinedKeyedThreeElementRange"
    class_name: ClassVar[str] = "RequiredMultivaluedInlinedKeyedThreeElementRange"
    class_model_uri: ClassVar[URIRef] = LISTS_AND_KEYS.RequiredMultivaluedInlinedKeyedThreeElementRange

    v1: Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.v1):
            self.MissingRequiredField("v1")
        self._normalize_inlined_as_dict(slot_name="v1", slot_type=KeyedThreeElementClass, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.optionalOneElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalOneElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalOneElementRange__v1, domain=None, range=Optional[Union[dict, OneElementClass]])

slots.requiredOneElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredOneElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredOneElementRange__v1, domain=None, range=Union[dict, OneElementClass])

slots.optionalOneElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalOneElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalOneElementRangeList__v1, domain=None, range=Optional[Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]]])

slots.requiredThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredThreeElementRangeList__v1, domain=None, range=Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]])

slots.optionalKeyedOneElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedOneElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedOneElementRange__v1, domain=None, range=Optional[Union[str, KeyedOneElementClassName]])

slots.optionalKeyedOneElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedOneElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedOneElementRangeList__v1, domain=None, range=Optional[Union[Union[str, KeyedOneElementClassName], list[Union[str, KeyedOneElementClassName]]]])

slots.optionalIdentifiedOneElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalIdentifiedOneElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalIdentifiedOneElementRange__v1, domain=None, range=Optional[Union[str, IdentifiedOneElementClassName]])

slots.optionalIdentifiedOneElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalIdentifiedOneElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalIdentifiedOneElementRangeList__v1, domain=None, range=Optional[Union[Union[str, IdentifiedOneElementClassName], list[Union[str, IdentifiedOneElementClassName]]]])

slots.optionalKeyedTwoElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedTwoElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedTwoElementRange__v1, domain=None, range=Optional[Union[str, KeyedTwoElementClassName]])

slots.optionalKeyedTwoElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedTwoElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedTwoElementRangeList__v1, domain=None, range=Optional[Union[Union[str, KeyedTwoElementClassName], list[Union[str, KeyedTwoElementClassName]]]])

slots.optionalKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedThreeElementRange__v1, domain=None, range=Optional[Union[str, KeyedThreeElementClassName]])

slots.optionalKeyedThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalKeyedThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalKeyedThreeElementRangeList__v1, domain=None, range=Optional[Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]]])

slots.requiredIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredIdentifiedThreeElementRange__v1, domain=None, range=Union[str, IdentifiedThreeElementClassName])

slots.requiredIdentifiedThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredIdentifiedThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredIdentifiedThreeElementRangeList__v1, domain=None, range=Union[Union[str, IdentifiedThreeElementClassName], list[Union[str, IdentifiedThreeElementClassName]]])

slots.requiredKeyedThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredKeyedThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredKeyedThreeElementRangeList__v1, domain=None, range=Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]])

slots.requiredInlinedIdentifiedOneElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredInlinedIdentifiedOneElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredInlinedIdentifiedOneElementRangeList__v1, domain=None, range=Union[list[Union[str, IdentifiedOneElementClassName]], dict[Union[str, IdentifiedOneElementClassName], Union[dict, IdentifiedOneElementClass]]])

slots.entryList__entries = Slot(uri=LISTS_AND_KEYS.entries, name="entryList__entries", curie=LISTS_AND_KEYS.curie('entries'),
                   model_uri=LISTS_AND_KEYS.entryList__entries, domain=None, range=Optional[Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]]])

slots.optionalThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalThreeElementRange__v1, domain=None, range=Optional[Union[dict, ThreeElementClass]])

slots.requiredThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredThreeElementRange__v1, domain=None, range=Union[dict, ThreeElementClass])

slots.optionalIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalIdentifiedThreeElementRange__v1, domain=None, range=Optional[Union[str, IdentifiedThreeElementClassName]])

slots.requiredKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredKeyedThreeElementRange__v1, domain=None, range=Union[str, KeyedThreeElementClassName])

slots.optionalInlinedKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalInlinedKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalInlinedKeyedThreeElementRange__v1, domain=None, range=Optional[Union[dict, KeyedThreeElementClass]])

slots.requiredInlinedIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredInlinedIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredInlinedIdentifiedThreeElementRange__v1, domain=None, range=Union[dict, IdentifiedThreeElementClass])

slots.optionalInlinedAsListKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalInlinedAsListKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalInlinedAsListKeyedThreeElementRange__v1, domain=None, range=Optional[Union[dict, KeyedThreeElementClass]])

slots.requiredInlinedAsListIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredInlinedAsListIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredInlinedAsListIdentifiedThreeElementRange__v1, domain=None, range=Union[dict, IdentifiedThreeElementClass])

slots.optionalMultivaluedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalMultivaluedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalMultivaluedThreeElementRange__v1, domain=None, range=Optional[Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]]])

slots.requiredMultivaluedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredMultivaluedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredMultivaluedThreeElementRange__v1, domain=None, range=Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]])

slots.optionalMultivaluedKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalMultivaluedKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalMultivaluedKeyedThreeElementRange__v1, domain=None, range=Optional[Union[Union[str, KeyedThreeElementClassName], list[Union[str, KeyedThreeElementClassName]]]])

slots.requiredMultivaluedIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredMultivaluedIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredMultivaluedIdentifiedThreeElementRange__v1, domain=None, range=Union[Union[str, IdentifiedThreeElementClassName], list[Union[str, IdentifiedThreeElementClassName]]])

slots.optionalMultivaluedInlinedListIdentifiedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalMultivaluedInlinedListIdentifiedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalMultivaluedInlinedListIdentifiedThreeElementRange__v1, domain=None, range=Optional[Union[dict[Union[str, IdentifiedThreeElementClassName], Union[dict, IdentifiedThreeElementClass]], list[Union[dict, IdentifiedThreeElementClass]]]])

slots.requiredMultivaluedInlinedListKeyedThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredMultivaluedInlinedListKeyedThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredMultivaluedInlinedListKeyedThreeElementRangeList__v1, domain=None, range=Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]])

slots.optionalMultivaluedInlinedIdentifiedThreeElementRangeList__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="optionalMultivaluedInlinedIdentifiedThreeElementRangeList__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.optionalMultivaluedInlinedIdentifiedThreeElementRangeList__v1, domain=None, range=Optional[Union[dict[Union[str, IdentifiedThreeElementClassName], Union[dict, IdentifiedThreeElementClass]], list[Union[dict, IdentifiedThreeElementClass]]]])

slots.requiredMultivaluedInlinedKeyedThreeElementRange__v1 = Slot(uri=LISTS_AND_KEYS.v1, name="requiredMultivaluedInlinedKeyedThreeElementRange__v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.requiredMultivaluedInlinedKeyedThreeElementRange__v1, domain=None, range=Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]])

slots.v1 = Slot(uri=LISTS_AND_KEYS.v1, name="v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.v1, domain=None, range=Union[Union[dict, TwoElementClass], list[Union[dict, TwoElementClass]]])

slots.RequiredOneElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredOneElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredOneElementRangeList_v1, domain=RequiredOneElementRangeList, range=Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]])

slots.RequiredTwoElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredTwoElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredTwoElementRangeList_v1, domain=RequiredTwoElementRangeList, range=Union[Union[dict, TwoElementClass], list[Union[dict, TwoElementClass]]])

slots.RequiredInlinedOneElementRange_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedOneElementRange_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedOneElementRange_v1, domain=RequiredInlinedOneElementRange, range=Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]])

slots.RequiredInlinedOneElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedOneElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedOneElementRangeList_v1, domain=RequiredInlinedOneElementRangeList, range=Union[Union[dict, OneElementClass], list[Union[dict, OneElementClass]]])

slots.RequiredInlinedTwoElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedTwoElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedTwoElementRangeList_v1, domain=RequiredInlinedTwoElementRangeList, range=Union[Union[dict, TwoElementClass], list[Union[dict, TwoElementClass]]])

slots.RequiredInlinedThreeElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedThreeElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedThreeElementRangeList_v1, domain=RequiredInlinedThreeElementRangeList, range=Union[Union[dict, ThreeElementClass], list[Union[dict, ThreeElementClass]]])

slots.RequiredInlinedKeyedOneElementRange_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedOneElementRange_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedOneElementRange_v1, domain=RequiredInlinedKeyedOneElementRange, range=Union[list[Union[str, KeyedOneElementClassName]], dict[Union[str, KeyedOneElementClassName], Union[dict, KeyedOneElementClass]]])

slots.RequiredInlinedKeyedOneElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedOneElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedOneElementRangeList_v1, domain=RequiredInlinedKeyedOneElementRangeList, range=Union[list[Union[str, KeyedOneElementClassName]], dict[Union[str, KeyedOneElementClassName], Union[dict, KeyedOneElementClass]]])

slots.RequiredInlinedKeyedTwoElementRange_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedTwoElementRange_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedTwoElementRange_v1, domain=RequiredInlinedKeyedTwoElementRange, range=Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]])

slots.RequiredInlinedKeyedTwoElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedTwoElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedTwoElementRangeList_v1, domain=RequiredInlinedKeyedTwoElementRangeList, range=Union[dict[Union[str, KeyedTwoElementClassName], Union[dict, KeyedTwoElementClass]], list[Union[dict, KeyedTwoElementClass]]])

slots.RequiredInlinedKeyedThreeElementRange_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedThreeElementRange_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedThreeElementRange_v1, domain=RequiredInlinedKeyedThreeElementRange, range=Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]])

slots.RequiredInlinedKeyedThreeElementRangeList_v1 = Slot(uri=LISTS_AND_KEYS.v1, name="RequiredInlinedKeyedThreeElementRangeList_v1", curie=LISTS_AND_KEYS.curie('v1'),
                   model_uri=LISTS_AND_KEYS.RequiredInlinedKeyedThreeElementRangeList_v1, domain=RequiredInlinedKeyedThreeElementRangeList, range=Union[dict[Union[str, KeyedThreeElementClassName], Union[dict, KeyedThreeElementClass]], list[Union[dict, KeyedThreeElementClass]]])
