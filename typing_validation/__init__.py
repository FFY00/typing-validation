"""
    Runtime validation using type hints.
"""

__version__ = "1.1.0"

from .inspector import TypeInspector, UnsupportedType
from .validation import validate, can_validate, validation_aliases, validated, validated_iter
from .validation_failure import get_validation_failure, latest_validation_failure
from .descriptor import Descriptor

# re-export all encodings and functions.
__all__ = [
    "validate", "can_validate", "validation_aliases", "validated", "validated_iter",
    "TypeInspector", "UnsupportedType",
    "get_validation_failure", "latest_validation_failure", "Descriptor"
]
