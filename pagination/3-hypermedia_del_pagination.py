#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: row for i, row in enumerate(dataset)
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient hypermedia pagination structure."""
        data = self.indexed_dataset()
        max_key = max(data.keys())

        assert index is not None
        assert isinstance(index, int)
        assert index >= 0
        assert index <= max_key

        page_data = []
        current = index

        while len(page_data) < page_size and current <= max_key:
            if current in data:
                page_data.append(data[current])
            current += 1

        next_index = current if current <= max_key else None

        return {
            "index": index,
            "data": page_data,
            "page_size": len(page_data),
            "next_index": next_index,
        }
