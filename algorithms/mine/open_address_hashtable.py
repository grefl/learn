import unittest
import random
from pathlib import Path

class HashTable:
    def __init__(self, size = 100):
        self.size = size * 2
        self.array = [None] * self.size

        self.large_int       = self.gen_large_int()
        self.P = self.gen_large_prime(self.large_int)
        self.A= random.randint(0, self.P-1) #Note(greg) should this be prime-1?

        
    def hash(self, current_key):

        k = sum([ord(c) for c in current_key])
        hashed_key = ((k*self.A) % self.P) % self.size
        return hashed_key

    def gen_large_int(self):
        return random.randint(2**16, 2**32)

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

class Test(unittest.TestCase):
    def test_1(self):
        h = HashTable()
        h.insert("GORB", "I am GORB!")
        h.insert("Hollow knight", "10/10")
        h.insert("GORB1", "I am not GORB!")
        self.assertEqual(h.get("GORB"), "I am GORB!")

if __name__ == "__main__":
    unittest.main()

