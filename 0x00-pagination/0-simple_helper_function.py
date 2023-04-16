#!/usr/bin/env python3
"""define index_range function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''
    return tuple containing start index and end index
    args:
        page(int): page number
        page_size(int): number of elements in the data fetched
    '''
    start_index = (page * page_size) - page_size
    end_index = page * page_size
    return (start_index, end_index)
