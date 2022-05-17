from random import randrange 

def swap(a, i,j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

a = [1, 2, 30, 12, 11]

def quicksort(a, l, r):
    print(a, l, r)
    if r- l <= 1:
     return
    x = a[randrange(l, r)]
    m = l
    for i in range(l, r):
     if a[i] < x:
      swap(a, i, m)
      m +=1
    quicksort(a, l,m)
    quicksort(a, m, r)
quicksort(a,0, len(a))
