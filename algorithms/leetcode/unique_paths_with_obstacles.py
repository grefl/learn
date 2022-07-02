import unittest
def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    
    num_ways = [[0 for _ in range(n)] for _ in range(m)]
    starting_value = -1 if obstacleGrid[0][0] == 1 else 1 
    num_ways[0][0] = starting_value
    
    for col in range(1, n):
        if obstacleGrid[0][col] == 1 or num_ways[0][col-1] == -1:
            num_ways[0][col] = -1
        else:
            num_ways[0][col] = 1
    for row in range(1, m):
        if obstacleGrid[row][0] == 1 or num_ways[row-1][0] == -1:
            num_ways[row][0] =  -1
        else:
            num_ways[row][0] = 1
    
    
    for row in range(1, m):
        for col in range(1, n):
            if obstacleGrid[row][col] == 1 or (num_ways[row-1][col] == -1 and num_ways[row][col-1]  == -1):
                num_ways[row][col] = -1
            elif num_ways[row-1][col] == -1:
                num_ways[row][col] = num_ways[row][col-1]
            elif num_ways[row][col-1] == -1:
                num_ways[row][col] = num_ways[row-1][col]
            else:
                num_ways[row][col] = num_ways[row][col-1] + num_ways[row-1][col]
    last = num_ways[m-1][n-1]
    return last if last > 0 else 0 

class Test(unittest.TestCase):

    def test_1(self):
        should_be = 2 
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        actual = uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(should_be, actual)

if __name__ == "__main__":
    unittest.main()

