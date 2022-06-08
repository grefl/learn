import math

def max_sub_array(nums):
    if len(nums) == 1:
        return nums[0]

    best = -math.inf
    current = 0
    for num in nums:
        current += num
        best    = max(best, current)
        current = max(0, current)
    return best



print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))

