import unittest
from collections import deque

def invertTree(root):
    """
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
    -------------------------------------
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
    -------------------------------------
    """

    if root is None:
        return None

    temp       = root.left
    root.left  = root.right
    root.right = temp 
    invertTree(root.left)
    invertTree(root.right)
    return root

def invertTreeIterative(root):
    if root is None:
        return None
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        temp = node.left
        node.left = node.right
        node.right = temp
        if node.left is not None:
            q.append(node.left) 
        if node.right is not None:
            q.append(node.right) 
    return root

def unwind(root):
    res = []
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node is None:
            return queue
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return res

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Test(unittest.TestCase):

    def test_1(self):

        tree = TreeNode(4, TreeNode(2), TreeNode(7))
        invertTree(tree)
        self.assertEqual([4,7,2], unwind(tree))
    def test_2(self):
        tree = TreeNode(4, TreeNode(2, TreeNode(1)), TreeNode(7))
        invertTreeIterative(tree)

        self.assertEqual([4,7,2,1], unwind(tree))

if __name__ == "__main__":
    unittest.main()
