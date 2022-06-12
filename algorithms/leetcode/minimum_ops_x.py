


def minimum_operations(nums, x):
    steps = 0
    lpointer = 0
    rpointer= len(nums) -1
    while lpointer <= rpointer:
        left  = nums[lpointer]
        right = nums[rpointer]
        if (left >= right and left <= x):
           lpointer +=1 
           x -= left
        elif right >= left and right <=x:
            rpointer -=1
            x -= right
        elif right <=x:
            rpointer -=1
            x -= right
        elif left > x:
            lpointer += 1
        elif right > x:
            rpointer -= 1
        steps +=1
        if x == 0:
            return steps
        if x < 0:
            return -1 
    return -1

def test(nums, x):
    x = {}
    for i in nums:
        if i in x:
            x[i] +=1
        else:
            x[i] = 1
    for i in nums:
        diff = x - i
        if diff in x and x[diff] > 0:
            x -=diff
        steps +=1

def minOperationsGreg(nums, target):
    if sum(nums) < target:
        return -1
    m = {} 
    m[0] = 0
    left = 0
    right = len(nums)-1
    curr1 = 0
    curr2 = 0 
    INF = 10 ** 20
    best = INF 
    while left < right:
        curr1 += nums[left] 
        curr2 += nums[right] 
        m[curr1] = left + 1
        left +=1
        right -=1
        if target in m:
            best = min(best, m[target])
        if target - curr2 in m:
            best = min(best, m[target-curr2] + left)
    return best if best != INF else -1

def minOperationsLarry(nums, target):
    if sum(nums) < target:
        return -1
    m = {}
    m[0] = 0
    curr = 0
    for idx, num in enumerate(reversed(nums), 1):
        curr += num
        m[curr] = idx
    INF = 10 ** 20
    best = INF
    if target in m:
        best = min(best, m[target])
    curr = 0

    for idx, num in enumerate(nums, 1):
        curr += num
        if target - curr in m:
            best = min(best, m[target-curr] + idx)
    return best if best != INF else -1


def minOperationsSlidingWin(nums, target):
    [1,1,4,3,2]
    s = sum(nums) - target
    if s < 0: 
        return -1
    if s == 0:
        return len(nums)
    start = curr = 0
    length = -1
    for end in range(len(nums)):
        curr += nums[end]
        while curr >= s:
            print(f"curr {curr} {nums[start]}")
            if curr == s:
                print('hi')
                print(s, curr)
                print(length)
                length = max(length, end-start+1)
                print(length)
            curr -= nums[start]
            start +=1
    return length if length == -1 else len(nums) - length
if __name__ == "__main__":

    nums = [1,1,4,3,2]
    x = 5
    print(minOperationsLarry(nums, x))
    nums = [3,2,4,2,3]
    x = 1 
    print(minOperationsLarry(nums, x))
    nums = [11,11,4,2,3, 2, 5,1,2,33, 512, 123, 4, 5,6,7,7,7,7] 
    x = 1 
    print(minOperationsLarry(nums, x))
    nums = [1,1,4,2,3]
    x = 5
    print(minOperationsGreg(nums, x))
    nums = [1,1,4,2,3]
    x = 5
    print(minOperationsSlidingWin(nums, x))
