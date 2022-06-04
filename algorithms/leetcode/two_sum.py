

def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    m = {}
    for i,n in enumerate(nums):
        diff = target - n
        m[diff] = i

    for i, n in enumerate(nums):
        if n in m:
            return [i, m[n]]
    return [-1, -1]

def two_sum_simple(nums, target):
    m = {}
    for i,n in enumerate(nums):
        if n in m:
            return [i, m[n]]
        diff = target - n
        m[diff] = i
    return [-1, -1]

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    res_1 = two_sum(nums, target)
    res_2 = two_sum_simple(nums, target)
    print(res_1, res_2)

