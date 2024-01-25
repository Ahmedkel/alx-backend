#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page, page_size):
    """index_range function"""
    page -= 1
    start_index = page * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
