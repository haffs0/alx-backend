#!/usr/bin/env python3
"""hypermedia pagination"""
import csv
import math
from typing import Tuple, List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """list of rows"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        try:
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """retrieve full info"""
        data = self.get_page(page, page_size)
        all_data = len(self.dataset())
        total_pages = math.ceil(all_data / page_size)
        next_page = None
        prev_page = None
        if (page + 1) < total_pages:
            next_page = page + 1
        if (page - 1) != 0:
            prev_page = page - 1
        return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
        }
