#!/usr/bin/env python3
"""
Module 4-tasks:
Execute multiple task_wait_random tasks concurrently and collect their delays.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return a list of
    delays in ascending order without using sort().
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
