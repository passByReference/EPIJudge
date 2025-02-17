from typing import List

from test_framework import generic_test
   

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.
    if len(A) == 0 or len(B) == 0 or A[0] > B[-1] or A[-1] < B[0]: 
        return []
    iter1, iter2 = 0,0
    result = []
    # while iter1 < len(A) and A[iter1] < B[iter2]:
    #     iter1 += 1
    # if iter1 >= len(A):
    #     return result
    while iter2 < len(B) and iter1 < len(A):
        if A[iter1] == B[iter2]:
            if len(result) == 0 or result[-1] != A[iter1]: 
                result.append(A[iter1])
            iter1 += 1
            iter2 += 1
        elif A[iter1] > B[iter2]:
            iter2 += 1
        else:
            iter1 += 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
