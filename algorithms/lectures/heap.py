

# This heap is dump but it works
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



h = Heap()
h.insert(10)
h.insert(20)
h.insert(2)
print(h.remove_min())
print(h.remove_min())
h.insert(1)
print(h.remove_min())

