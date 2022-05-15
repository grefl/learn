

def swap(array, i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

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


class GoodHeap():

    def __init__(self):
        self.a = []
        self.n = 0

    def insert(self, x):
        self.a.append(x)
        self.n +=1
        i = self.n-1 
        # works
        while i > 0 and (self.a[i] < self.a[(i-1)//2]):
            swap(self.a, i, (i-1)//2)
            i = (i-1)//2 
    def smallest_child_index(self, i):
        i1 = (2*i)+1
        i2 = (2*i)+2
        if i1 >= self.n-1 or i2 > self.n-1:
            return None
        if self.a[i1] < self.a[i2]:
            return i1 
        else:
            return i2 
        

    def remove_min(self):
        if self.n == 0:
            return None
        self.n -=1
        end = self.a.pop()
        if len(self.a) == 0:
            return end
        smallest = self.a[0]
        self.a[0] = end
        i = 0
        while i < self.n:
            child_index = self.smallest_child_index(i)
            if child_index is None:
                break
            if self.a[child_index] < self.a[i]:
                swap(self.a, child_index, i)
            i = child_index 
        return smallest 

if __name__ == "__main__":
    # 1
    h = DumbHeap()
    h.insert(10)
    h.insert(20)
    h.insert(2)
    print(h.remove_min())
    print(h.remove_min())
    h.insert(1)
    print(h.remove_min())

    # 2
    h2 = DumbHeap2()
    h2.insert(10)
    h2.insert(20)
    h2.insert(2)
    print(h2.remove_min())
    print(h2.remove_min())
    h2.insert(1)
    print(h2.remove_min())


    # 3 
    gh = GoodHeap()
    gh.insert(100)
    gh.insert(10)
    gh.insert(1)
    gh.insert(999)
    gh.insert(130)
    gh.insert(11)
    print('good heap')
    print(gh.remove_min())
    print(gh.remove_min())
    print(gh.remove_min())
    print(gh.remove_min())
    print(gh.remove_min())
    print(gh.remove_min())
