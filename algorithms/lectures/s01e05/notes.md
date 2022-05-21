# Binary Search



## Basic binary search
O(lgn) search time
However, this is a waste of time. Just put it in a hashmap and you'll get O(1) look up time
```python
a = [2,11,30,31,40]


def bs(a,l,r,x):
  m = (l+r) // 2
  if a[m] == x:
    return m
  elif array[m] < x:
    return bs(a, m+1, r,x)
  elif array[m] > x:
    return bs(a,l, m-1,x)
  else:
    return None

```


## Binary search for elements >= x
a = [2,11,30,31,40]
x = 30

We want to return all elements greater than or equal to x.

In order to do this we should move two pointers around. l and r.

At the end we will return r

We will also need to set l and r to indexes outside of the array. l -1 and r = len(a)

```python

def bs_gtx(a, x):
  l = -1
  r = len(a)

  m = (l+r) // 2
  while r > l+1:
    if a[m] >= x:
      r = m
    else:
      l = m
  return r
```
if x is not in the array then r will return len(a)

If you want to do the opposite - that is, return all numbers than are <= x then you need to change your comparison and return l instead


```python

def bs_lei(a, x):
  l = -1
  r = len(a)

  m = (l+r) // 2
  while r > l+1:
    if a[m] > x:
      r = m
    else:
      l = m
  return r
```


## Summary

Think of it like this. You want to find the minimum good number. So you mark all numbers to the left of x as bad and all numbers to the right of x as good.
