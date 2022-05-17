from pathlib import Path
import random 
import unittest
from heap import GoodHeap



class TestHeap(unittest.TestCase):
    def test_list_same(self):
        gh = GoodHeap()
        collect = []
        check = []
        for i in range(50000):
            num = random.randint(0, 700000)
            gh.insert(num)
        for i in range(50000):
            num = gh.remove_min()
            check.append(num)
            collect.append(num)
        
        check = sorted(check)
        self.assertTrue(check == collect)
if __name__ == "__main__":
    unittest.main()
