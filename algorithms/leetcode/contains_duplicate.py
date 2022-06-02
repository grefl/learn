import unittest


def contains_duplicate(input):
    """
    Given an integer array nums, return true
    if any value appears at least twice in 
    the array, and return false if every 
    element is distinct.
    
    Input: nums = [1,2,3,1]
    Output: true
    """
    s = set()

    for v in input:
        if v in s:
            return False
        s.add(v) 
    return True


class Test(unittest.TestCase):

    def test_should_be_false(self):
        input = [1,2,3,4,1]
        i_am_false = contains_duplicate(input)
        self.assertFalse(i_am_false)



if __name__ == "__main__":
    unittest.main()

