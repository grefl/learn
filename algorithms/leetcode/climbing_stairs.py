# Dynamic programming
# Type: How many?


def climbStairs(n, cache={}):
    if n in cache:
        return cache[n]
    if n == 0:
        return 1 
    if n < 0:
        return 0 
    cache[n] = climbStairs(n-1, cache) + climbStairs(n-2, cache)
    return cache[n]


res = climbStairs(900)
print(res)
