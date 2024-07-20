#!/usr/bin/env python3
"""Utility function for handling pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Gets the index range based on the specified page and page size
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
