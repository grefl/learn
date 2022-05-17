## What is the problem?

We are given some array
And we need to find a particular value at index k.

Solution. Sort array and then get the element -> O(nlgn)


**Alternative** we can be faster than this.

```python

k = 4
a = [12, 3, 2, 33, 48,74,1]

find(l,r,k):
  # l<=k<r
  if r-l == 1: return a[k]

  x = a[random(l..r)]
  m = l
  for i in range(l, r):
  if a[i] < x:
    swap(a, i,m)
    m +=1
   if k < m:
    return find(l,m,k)
   else
    return find(m,r,k)
```

