import pprint
from queue import deque

class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left  = left
        self.right = right





def tree_stuff():
    tree = Node('parent', Node('left', Node('leaf')), Node('right', Node('leaf2'), Node('leaf3')))
    queue = deque()
    queue.append(tree)
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

if __name__ == "__main__":
    nodes = tree_stuff()
    pprint.pprint(nodes, indent=4)

