# Hashing Introduction - Some notes for ya

## What Hashing?

What is hashing? If you need to store something in a database-like structure AND you need to store a key (k) and assign it to a value (v), then hashing is for you. For python programmers, this is dictionary ```d = {}```, for JavaScripters (?) it's an object  ```let m = {}```, and for Rustaceans its ```let mut m = HashMap::new()```. The thing they share in common is that they're using some kind of hashing function that tries to create a unique index from this key and then assign the key and value to the array. Since the hash function is also use for the get method, we can be certain that we'll get back the same value when using the same key.

Example. 

```python
name = 'GORB'
saying = 'I am GORB!'
hashtable = {} # python people call it a dictionary or dict but it's all the same
hashtable[name] = saying

print(hashtable[name]) # 'I am GORB!'
```

But of course nothing is so simple as this. There is a catch, it's very easy to make a hashing function ```def hash(key): return sum([ord(c) * 31 for c in key]) % len(self.array)``` but it's hard to make it evenly distribute across your array. What if two different keys that are passed through your hash function end up creating the same key? ```[hash(key) for key in ['GORB', 'BORG']]``` create the same key when using our simple hash function. We have a problem - a collision. So now we need a collision policy - that is, what to do when two different keys create the same index when passing through our hash function? As far as I can tell, this is a problem for all hash functions that aim for performance, since you can't guarentee that you won't end up with a collision no matter how fancy your hashing function is. So you better have a collision policy that doesn't ruin the O(1) look up time for your HashTable.

Luckily there are a few methods. The simplest one is to loop through your array until you find an empty slot. Then you insert the (key, value) into that slot. Then when you ```get(key)``` that same hash function runs over the key, gets the index, and we loop until we see the `current_key == prev_key`.

```python
# first figure out what space we'll need - let's assume will be inserting 10 keys. num_keys = 10
# so the length of the array should be 2*num_keys
num_keys = 10
array = [None] * (2*num_keys)
def insert(curreny_key, value):
    index = hash(current_key)
    while array[index] is not None:
        index = (index + 1) % self.size
    array[index] = (current_key, value)
    return True

def get(current_key):
    index = hash(current_key)
    while array[index] is not None:
        if array[index][0] == current_key:
            return array[index][1]
        index = (index + 1) % size
    return None 
```


Now if our hash function is good we will evenly distribute each key across the array. And if there is a collision we shall just loop until we find a free spot, then we assign the (key, value) into the array. Now, when we look up the key we can double check that the keys match before returning the value.


## Collisions - the bane of hash tables

In a perfect world a hashtable would receive a well distributed input of keys (perhaps random numbers) but real life is on hard mode so no dice. Instead, the input of of keys is usually clustered and means that our poor hash function will have a hard time allocating similar keys to different parts of the array. So we're going to end up with collisions whether we like it or not. 

To illustrate this, consider that most data is structure in some way or other, otherwise it's just random noise. So when receiving keys and hashing them, we're going to have to deal with the patterns that end up skewing the distribution of our hashed_indexes. 


### Interesting points

- If domain is unknown, then try to make a function that isn't sensitive to the lower or higher bits of the incoming keys.
- If the domain is known, then try to avoid using the known skewed input. Example, don't use the first letter of english words since it is unevenly distributed.


