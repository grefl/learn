import unittest


class DumbHashTable:
    def __init__(self, size=10):
        self.array = [(None, None)] * size
        self.size = size

    def hash(self, current_key):
        hashed_key = sum([ord(c) for c in current_key]) % self.size
        return hashed_key
    def insert(self, current_key, value):
        hashed_key = self.hash(current_key)
        self.array[hashed_key] = (current_key, value)
        return value
    def get(self, current_key):
        hashed_key = self.hash(current_key)
        (prev_key, value) = self.array[hashed_key]
        if prev_key is None or prev_key != current_key:
            return None
        (_, value) = self.array[hashed_key]
        return value 

            
class Test(unittest.TestCase):
    def test_1(self):
        h = DumbHashTable()
        h.insert("hi", 123)
        h.insert("gorb", "I am GORB!")
        self.assertEqual(h.get('hi'), 123)
        self.assertEqual(h.get('gorb'), "I am GORB!") 

        h.insert("hi", 1)
        self.assertEqual(h.get('hi'), 1)
        for i in range(100):
            h.insert(str(i), i)
        self.assertEqual(h.get('hi'), None)

if __name__ == "__main__":
    unittest.main()

