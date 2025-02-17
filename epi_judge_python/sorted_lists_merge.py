from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    iter1, iter2 = L1, L2
    head = ListNode(0)
    curr = head
    while iter1 and iter2:
        if iter1.data < iter2.data:
            curr.next = iter1
            iter1 = iter1.next
        else:
            curr.next = iter2
            iter2 = iter2.next
        curr = curr.next
    curr.next = iter1 if iter1 else iter2
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
