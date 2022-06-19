import unittest
def find_short(s):
    min_s = 10 ** 10
    for string in s.split(' '):
        if len(string) < min_s:
            min_s = len(string)
    return min_s 



class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
if __name__ == "__main__":
   unittest.main() 
