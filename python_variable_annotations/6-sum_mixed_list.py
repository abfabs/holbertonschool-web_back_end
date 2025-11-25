#!/usr/bin/env python3
"""Module 6-sum_mixed_list: type-annotated function sum_mixed_list that sums a list of ints and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all integers and floats in mxd_lst."""
    return sum(mxd_lst)
