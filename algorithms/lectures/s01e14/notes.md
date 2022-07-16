# Hash Tables

## Improve hashtable.get(key) speed

### Random hash function

Simple hash functions in hash tables tend to cause collisions. These collisions can be handled by inner lists that need to be traversed in order to find the element we want. But there is a cost and it likely will come from having many keys can are similar enough that they have the same hashed key value. So we end up with very large inner collision lists that end up being traversed in O(n) time.

To improve the speed of get operations, we need to use a better hash function. One such function is a random hash function. This is calculated beforehand with the size of the array (size=m) used. 

```python
hash_function = m^u values.
```

### Make a huge array

Another solution is too make an array that is so big that it is less likely to end up with collisions.
