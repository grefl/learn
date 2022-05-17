# Data structures: Binary Heap - Heap Sort



## Arrays

Getting an element and putting an element is O(1)


## Binary Heap

## Priority Queue

contains set of elements
insert(x)
remove_min()


### We can use an array to make a heap

Set to first n elements contain the elements of the heap set
Adding elements to the heap is as simple as adding to the array


> Fast insertion slow removal 
```python
  def insert(x):
    a[n] = x
    n++
   remove_min():
    j=0
    for i in range(n):
    if a[i] < a[j]
      j = i
    swap(a[j], a[n-1])
    n --
    return a[n]
```


> Sorted array, this is good because the minimal element is always at the end
> Fast removal slow insertion 

```python
# O(1)
def remove_min(self):
  self.n -=1
  return self.a[self.n]
# O(n)
def insert(self,x):
  self.a[self.n] =  x
  self.n +=1
  i = self.n-1
  while i > 0 and self.a[i] > self.a[i-1]:
    self.swap(self.n, i, i-1)
    i -=1
```

> Binary heap
```python

child_1 = 2*(i+1) 
child_2 = 2*(i+2)
def insert(self,x):
  self.a[self.n] = x
  self.n+=1
  i = 0
  while i < self.n-1 and (self.a[i] < self.a[(i-1)/2):
    swap(self.n, i, (i-1)/2)
      i = (i-1) / 2
def remove_min(self):
  self.n
  self.a
  

```

you have to insert at the end of the array and then insert up (bubble up) until you have satisfied the condition = element is greater than the parent but is less than it's children
## Heap takeaways

1. Heaps (due to their use cases) usually have the same amount of inserts and removals


## Ways to test your algorithm

First make a table of the methods with their time complexity. Then test them out by running O(n) operations of that method. You'll find that the methods that are O(n) suddenly don't look so good because they're now O(n^2)



