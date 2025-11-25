#!/usr/bin/env python3
"""Module 7-to_kv: type-annotated function to_kv that returns a tuple of a string and the square of a number."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v as a float."""
    return (k, float(v * v))
