
def diff(a, b):
    """
    Calculates the difference between two strings.
    It does this by checking the minimal number of changes required
    to convert one string to the other
    """
    ways = [[0 for _ in range(len(b))] for _ in range(len(a))]
    ways[0][0] = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0 or j == 0:
                ways[i][j] = i + j
                continue
            if a[i-1] == b[j-1]:
                ways[i][j] = ways[i-1][j-1] 
            else:
                ways[i][j] = min(ways[i-1][j-1], ways[i-1][j], ways[i][j-1]) + 1
    return ways[len(a)-1][len(b)-1]
res = diff('for i in range(2)', 'for i := range 2 {')
print(res)
