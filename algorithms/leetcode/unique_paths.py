import unittest

def uniquePaths(m, n):

    num_ways = [[0 for _ in range(n)] for _ in range(m)]
    num_ways[0][0] = 1 

    for j in range(1, n):
        num_ways[0][j] = 1

    for i in range(1, m):
        num_ways[i][0] = 1 

    for i in range(1, m):
        for j in range(1, n):
            num_ways[i][j] =  num_ways[i][j-1] + num_ways[i-1][j]

    return num_ways[m-1][n-1]




class Test(unittest.TestCase):

    def test_1(self):
        m = 3
        n = 7
        actual = uniquePaths(m,n)
        should_be = 28
        self.assertEqual(actual, should_be)

if __name__ == "__main__":
    unittest.main()
