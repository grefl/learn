import unittest


class DumbHashTable:
    def __init__(self, size=10):
        self.array = [[(None, None)] for _ in range(size)]
        print(self.array)
        self.size = size
    def getval(self,  array, current_key):

        for (key, value) in array:
            if key == current_key:
                return value
        return None
    def exists(self, array, current_key):
        for index,(key, _) in enumerate(array):
            if key == current_key:
                return index 
        return None 

    def hash(self, current_key):
        hashed_key = sum([ord(c) for c in current_key]) % self.size
        return hashed_key
    def insert(self, current_key, value):
        hashed_key = self.hash(current_key)
        index = self.exists(self.array[hashed_key], current_key)
        if index is None:
            self.array[hashed_key].append((current_key, value))
        else:
            self.array[hashed_key][index] = (current_key, value) 
        
        return value
    def get(self, current_key):
        hashed_key = self.hash(current_key)
        array = self.array[hashed_key]
        print(f"{array=}")
        value = self.getval(array, current_key)
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
        self.assertEqual(h.get('hi'), 1)

if __name__ == "__main__":
    unittest.main()

