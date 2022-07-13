import unittest
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(node):
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


    Example 1:
    ==============================================
        Input: root = [3,9,20,null,null,15,7]
        Output: 3
    ==============================================
    """
    if node is None:
        return 0
     
    depth = max(maxDepth(node.left), maxDepth(node.right)) + 1
    return depth 

def maxDepthIter(root):
    # FIXME: doesn't work on all trees
    if root is None:
        return 0
    current_depth = max_depth = 0 
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
        if node.right is None and node.left is None:
            print('here')
            max_depth = max(max_depth, current_depth)
            current_depth = 0 
            continue
        current_depth +=1
        max_depth = max(max_depth, current_depth)
    return max_depth + 1 

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

class Test(unittest.TestCase):

    def test_1(self):
        tree = Node(1, None, Node(2, Node(3), Node(5, Node(1, Node(2, Node(1, Node(3, Node(2, Node(1, Node(1, Node(1)))))))))))
        depth = maxDepth(tree)

        self.assertEqual(depth, 11)
    def test_2(self):

        tree = Node(1, None, Node(2, Node(3), Node(5, Node(1, Node(2, Node(1, Node(3, Node(2, Node(1, Node(1, Node(1)))))))))))
        depth = maxDepthIter(tree)

        self.assertEqual(depth, 11)

if __name__ == "__main__":
    unittest.main()
