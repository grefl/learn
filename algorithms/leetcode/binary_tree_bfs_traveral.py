import pprint
import unittest
from queue import deque

class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right


def levelOrder(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values. 
    (i.e., from left to right, level by level).

    Example
    ==========================================
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]
    ==========================================

    """
    if not root:
        return []

    queue = deque()
    queue.append(root)
    big = []

    while queue:
        small = []
        for _ in range(len(queue)):

            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            small.append(node.value)

        big.append(small) 

    return big

class Test(unittest.TestCase):

    def test_1(self):
        tree = Node('parent', Node('left', Node('leaf')), Node('right', Node('leaf2'), Node('leaf3')))
        expected = [['parent'], ['left', 'right'], ['leaf', 'leaf2', 'leaf3']]
        actual = levelOrder(tree)
        self.assertEqual(actual, expected)

    def test_2(self):
        tree = None 
        expected = []
        actual = levelOrder(tree)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

