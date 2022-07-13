def isSameTree(a, b):
    if a == b:
        return True
    q = deque()
    q.append(a)
    q.append(b)
    while q:
        n1 = q.popleft()
        n2 = q.popleft()
        if n1 is None or n2 is None:
            return False
        if n1.val != n2.val:
            return False
        if n1.left or n2.left:
            if n1.left is None or n2.left is None:
                return False
            q.append(n1.left)
            q.append(n2.left)
        if n1.right or n2.right:
            if n1.right is None or n2.right is None:
                return False
            q.append(n1.right)
            q.append(n2.right)
    return True


