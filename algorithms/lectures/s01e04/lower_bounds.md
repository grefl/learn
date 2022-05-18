# S01e04

So far we've done done sorting algorithms - mergesort, heapsort, quicksort. They're all `nlgn`. 


Can we go faster than this? Short answer - no.

But the issue is that you have to prove that all sort algorithms cannot go faster than `nlgn`



find the order of `x y z` 


```python
def find_order(x,y,z)
  if x < y and x < z:
    if y < z: return x, y, z
    else: return x, z, y
    #...continue on with comparisons
    # it's a tree structure
```

In the above example you produce leaf nodes. They are the different outcomes of the algorithm. The result depends on the ordering of the elements.

We have n! (n factorial) iterations.

The minimum height is `T(n) >= lg(n!)`

You need to make `nlgn` comparisons at least. This is the lowerbound.


## Takeaway

This is a proof of the inability to go faster than `nlgn` for sorting algorithms. This is formally called **lower-bound**.

