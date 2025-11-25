#!/usr/bin/env python3
"""
Module 0-async_generator:
Asynchronous generator that yields 10 random numbers with 1-second delay.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yield 10 random floats between 0 and 10,
    waiting 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
