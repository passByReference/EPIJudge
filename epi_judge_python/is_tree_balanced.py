from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def get_height(tree: BinaryTreeNode) -> int:
    if tree == None:
        return 0
    else:
        return 1 + max(get_height(tree.left), get_height(tree.right))
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    if tree == None:
        return True
    left = get_height(tree.left)
    right = get_height(tree.right)
    if abs(left - right) <= 1:
        return is_balanced_binary_tree(tree.left) and is_balanced_binary_tree(tree.right)
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
