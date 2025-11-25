#!/usr/bin/env python3
"""Module 8-make_multiplier: type-annotated function that returns a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
