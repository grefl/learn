import unittest
import random
from pathlib import Path
from pprint import pformat
DEBUG = {
        }
class HashTable:
    def __init__(self, size = 100):
        self.size = size * 2 
        self.array = [None] * self.size

        self.large_int       = self.gen_large_int(self.size)
        self.P = self.gen_large_prime(self.large_int)
        self.S = self.gen_large_prime(self.large_int // 2)
        self.A= random.randint(0, self.P-1) #Note(greg) should this be prime-1?

        
    def hash(self, current_key):
        hashed_key = 3 
        for c in current_key:
            hashed_key = (hashed_key * 71) + ord(c)
            # hashed_key = hashed_key*31 + ord(c)
        #hashed_key = hashed_key % self.size
        # hashed_key = ((hashed_key*self.A) % self.P) % self.size
        if hashed_key in DEBUG:
            DEBUG[hashed_key].append(current_key)
        else:
            DEBUG[hashed_key] = [current_key]
        return hashed_key % self.size

    def gen_large_int(self, size):
        return random.randint(7, size // 2)

    def gen_large_prime(self, large_int):
        number = large_int
        while number % 2 == 0:
            number -=1
        return number

    def insert(self, current_key, value):
        index = self.hash(current_key)
        while self.array[index] is not None:
            index = (index + 1) % self.size
        self.array[index] = (current_key, value)
        return True

    def get(self, current_key):
        index = self.hash(current_key)
        while self.array[index] is not None:
            if self.array[index][0] == current_key:
                return self.array[index][1]
            index = (index + 1) % self.size
        return None 
    def debug(self):
        Path('./debug.txt').write_text(pformat(DEBUG, indent=2))

class Test(unittest.TestCase):
    def test_1(self):
        h = HashTable()
        h.insert("GORB", "I am GORB!")
        h.insert("Hollow knight", "10/10")
        h.insert("GORB1", "I am not GORB!")
        self.assertEqual(h.get("GORB"), "I am GORB!")

if __name__ == "__main__":
    unittest.main()

