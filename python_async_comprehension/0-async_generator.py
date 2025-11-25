#!/usr/bin/env python3
"""
0-async_generator module

Contains an asynchronous generator that loops 10 times, waits 1 second
each time, and yields a random float between 0 and 10.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loop 10 times, asynchronously wait 1 second each iteration,
    and yield a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
