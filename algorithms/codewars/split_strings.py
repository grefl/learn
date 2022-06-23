import unittest

def split_strings(string):
    if len(string) % 2 != 0:
        end = [string[i:i+2] for i in range(0, len(string)-1, 2)] 
        end.append(string[-1] + '_')
        return end
    return [string[i:i+2] for i in range(0, len(string), 2)]



class Test(unittest.TestCase):
    def test_1(self):
        should_equal = ['ab']
        string = 'ab'
        strings = split_strings(string)
        self.assertEqual(should_equal, strings)

    def test_2(self):
        should_equal = ['ab', 'c_']
        string = 'abc'
        strings = split_strings(string)
        self.assertEqual(should_equal, strings)

    def test_3(self):
        should_equal = ['as', 'df', 'ad', 's_']
        string = 'asdfads'
        strings = split_strings(string)
        self.assertEqual(should_equal, strings)

if __name__ == "__main__":
    unittest.main()
