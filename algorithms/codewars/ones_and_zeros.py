import unittest


def binary_array_to_number1(arr):
    """
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
    """

    length = len(arr)-1
    decimal_num = 0
    for idx,num in enumerate(arr):
        power = length - idx
        if num:
            decimal_num += 2**power
    return decimal_num

def binary_array_to_number2(arr):
    return sum(2**(len(arr)-1 -idx) for idx, num in enumerate(arr) if num)



class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(binary_array_to_number1([0, 0, 1,1]), 3)

    def test_2(self):
        self.assertEqual(binary_array_to_number2([0, 0, 1,1]), 3)



if __name__ == "__main__":
    unittest.main()
