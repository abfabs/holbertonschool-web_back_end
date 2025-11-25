#!/usr/bin/env python3
"""Module 5-sum_list: type-annotated function sum_list that sums a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of all floats in input_list."""
    return sum(input_list)
