

# This heap is dump but it works
# insertion is O(1)
# remove_min is O(n)
class DumbHeap():

    def __init__(self):
        self.a = []
        self.n = 0

    def swap(self, i,j):
        temp = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = temp

    def insert(self, x):
        self.a.append(x)
        self.n +=1

    def remove_min(self):
        j = 0
        for i in range(1, self.n):
            if self.a[i] < self.a[j]:
                j = i
        self.swap(j, self.n-1)
        self.n -=1
        res = self.a[self.n]
        self.a.pop()
        return res 



h = DumbHeap()
h.insert(10)
h.insert(20)
h.insert(2)
print(h.remove_min())
print(h.remove_min())
h.insert(1)
print(h.remove_min())

def swap(array, i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

class DumbHeap2():
    def __init__(self):
        self.a = []
        self.n = 0

    # O(1)
    def insert(self,x):
        self.n +=1 
        self.a.append(x)
        i = 0 
        while i < self.n-1 and (self.a[i] < self.a[i-1]):
            swap(self.a, i,i-1)
            i +=1
        
    # O(1)
    def remove_min(self):
        self.n -=1
        return self.a.pop()
h2 = DumbHeap2()
h2.insert(10)
h2.insert(20)
h2.insert(2)
print(h2.remove_min())
print(h2.remove_min())
h2.insert(1)
print(h2.remove_min())

