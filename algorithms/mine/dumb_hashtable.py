import unittest


class DumbHashTable:

    def __init__(self, size=10):
        self.array = [[(None, None)] for _ in range(size)]
        self.size = size
        self.inserts = 0

    def should_resize(self):
        return  (self.inserts / self.size) > 0.8

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
        hashed_key = (sum([ord(c) for c in current_key]) * 17)  % self.size
        return hashed_key

    def insert(self, current_key, value):
        hashed_key = self.hash(current_key)
        index = self.exists(self.array[hashed_key], current_key)

        if index is None:
            if not self.should_resize():
                self.inserts +=1 
                self.array[hashed_key].append((current_key, value))
            else:
                # potentially expensive operation

                old_array = self.array
                self.size = self.size * 10 + self.inserts
                self.inserts = 0
                self.array= [[(None, None)] for _ in range(self.size)]
                for inner_array in old_array:
                    for (prev_key, prev_value) in inner_array:
                        if prev_key is None:
                            continue
                        self.insert(prev_key, prev_value)
        else:
            self.array[hashed_key][index] = (current_key, value) 
        return value

    def get(self, current_key):
        hashed_key = self.hash(current_key)
        array = self.array[hashed_key]
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

if __name__ == "__main__":
    unittest.main()

