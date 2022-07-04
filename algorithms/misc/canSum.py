

def can_sum(target, numbers, cache):
    if target in cache:
        return cache[target]
    if target == 0:
        return True
    if target < 0:
        return False
     
    for number in numbers:
        diff = target-number
        if can_sum(diff, numbers, cache):
            cache[target] = True
            return True
    cache[target] = False
    return False
    

if __name__ == "__main__":
    target = 4000 
    numbers = [12, 5, 2, 6, 7]
    cache = {}
    res = can_sum(target, numbers, cache)
    print(res)
