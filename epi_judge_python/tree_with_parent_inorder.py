from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # TODO - you fill in here.
    result = []
    if not tree:
        return result
    curr = tree
    while curr.left:
        curr = curr.left
    while curr:
        result.append(curr.data)
        curr = curr.parent
        result.append(curr.data)
        if curr.right:
            resu
    
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
