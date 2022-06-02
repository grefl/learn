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
            return True 
        s.add(v) 
    return False 

#===============================
#     DIFFERENT SOLUTIONS
#===============================
def contains_duplicate_simple(input):
    # s = set
    # i = input
    # Sets don't contain duplicates. 
    # So, if we add all of i to s to s and check that 
    # len(s) < len(i), if True then there are duplicates, 
    # because we have only one reason to have less elements in
    # s and i, that is, Sets don't contain duplicates
    return len(set(input)) < len(input)

class Test(unittest.TestCase):

    def test_should_be_true(self):
        input = [1,2,3,4,1]
        i_am_true = contains_duplicate(input)
        i_am_also_true = contains_duplicate_simple(input)
        self.assertTrue(i_am_true)
        self.assertTrue(i_am_also_true)



if __name__ == "__main__":
    unittest.main()

