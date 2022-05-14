# Time complexity and merge sort
https://www.youtube.com/watch?v=oWgLjhM-6XE&list=PLrS21S1jm43igE57Ye_edwds_iL7ZOAG4



## What is an algorithm?

Basic structure.
Input data -> Agorithm -> Output data


### Time measured in operations

If we use time measured in seconds then we would not be able to reuse this on other platforms that perform slightly differently. Instead, we should use operations since these will be the same regardless of the platform. 
### Computational model 

RAM model


###  Recursive time complexity

this is O(n)
def f(n):
  if n == 0:
    return
  f(n-1)

this is O(log n)
def f(n):
  if n == 0:
    return
  f(n/2)


this is O(n)
def f(n):
  if n == 0:
    return
  f(n/2)
  f(n/2)

this is O(n^log3/2) - less than O(n^2) but more than O(n)
def f(n):
  if n == 0:
    return
  f(n/2)
  f(n/2)
  f(n/2)




## Sorting

### Insertion Sort

```python
  array = [...n] 
  for i in range(n):
    j = i
     while j > 0 and a[j] < a[j-1]:
       swap(a[j], a[j-1])
       j -=1
```

#### Time complexity

Best case = O(n). The while loop will not run since there are not elements to swap

Worst case = O(n^2) The while loop will loop from j to 0 for every iteration of the outer loop.



### Merge sort

Merge operation is the cool part of merge sort. 

Two arrays = a and b. We merge them in order into another array then we return that sorted array and continue on sorting elements from 2 arrays into one array and then finally at the end we have sorted all elements into one array. 

We need to break up the original array into small pieces and then merge them all back together


## Master theorem

g(n)
a = {g(n/8) g(n/8)...} + f(n)
if f(n) is slower than a then the time complexity is f(n) otherwise it is O(nlg a)



