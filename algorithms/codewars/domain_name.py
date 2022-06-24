import unittest

def domain_name(string):
    
    if '//' in string:
        string = string.split('//')[1]

    index = 1 if 'www' in string else 0
    string = string.split('.')
    return string[index]

    
     


class Test(unittest.TestCase):
    def test_1(self):
        string = 'https://www.google.com/asdf'
        actual = domain_name(string)
        should_be = 'google'
        self.assertEqual(should_be, actual)

    def test_2(self):
        string = 'https://google.com.au'
        actual = domain_name(string)
        should_be = 'google'
        self.assertEqual(should_be, actual)

    def test_3(self):
        string = 'http://github.com/carbonfive/raygun'
        actual = domain_name(string)
        should_be = 'github'
        self.assertEqual(should_be, actual)

def main():
    string = 'https://www.google.com.au'
    res = domain_name(string)
    print(res)
    string = 'www.google.com.au'
    res = domain_name(string)
    print(res)

if __name__ == "__main__":
    unittest.main()

