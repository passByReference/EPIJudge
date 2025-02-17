from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def helper(p: BinaryTreeNode, q: BinaryTreeNode) -> bool:
    if p == q: return True
    if p and q and p.data == q.data:
        return helper(p.left, q.right) and helper(p.right, q.left)
    return False
def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if not tree:
        return True
    return helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
