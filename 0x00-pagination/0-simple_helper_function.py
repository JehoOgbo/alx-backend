#!/usr/bin/env python3
"""
index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = page_size * page - page_size
    end_index = page_size * page
    return (start_index, end_index)
