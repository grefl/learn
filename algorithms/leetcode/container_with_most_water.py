import unittest

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        min_height = min(height[left], height[right])
        calc = min_height * (right - left)
        max_water = max(max_water, calc)
        if height[left] <= height[right]:
            left +=1
        else:
            right -=1
    return max_water


class Test(unittest.TestCase):

    def test_1(self):
        # INPUT
        height = [1,8,6,2,5,4,8,3,7]
        # OUTPUT
        res =  maxArea(height)

        should_equal = 49
        self.assertEqual(res, should_equal)

if __name__ == "__main__":
    unittest.main()
