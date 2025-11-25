#!/usr/bin/env python3
"""
Module 0-basic_async_syntax: asynchronous coroutine that waits a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random float delay between 0 and max_delay seconds and return it.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
