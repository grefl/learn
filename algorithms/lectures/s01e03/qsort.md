# Quick sort

> A part of the  Randomized Algorith family


We need to break up the main array in linear time

We break the array into two parts. We pick a random index and any value less than this index should be in the left array and anything greater in the right array.

```python
def sort(left, right):
   if right - left <=1:
     return
   x = a[random(left..right-1)]
   m = left

   for i in range(left, right-1):
     if a[i] < x:
      swap(a, i, m)
      m +=1
    sort(l,m)
    sort(m, l)
```

## Time complexity

> n*log*n
The time complexity is due to each call being of O(n) and there are logn recursive calls.

So in total it is nlogn

It shares this time complexity with mergesort 


You can improve the performance if you pick 3 random indexes and then choose the middle one. This increasing your odds of getting closer to the middle of the array.



