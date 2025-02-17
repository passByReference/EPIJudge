from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    low, high = 0, len(A) - 1
    result = -1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if A[mid] > k:
            high = mid - 1
        elif A[mid] < k:
            low = mid + 1
        else:
            result = mid
            high = mid - 1
    
    return result
   


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
