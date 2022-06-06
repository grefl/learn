


def product_except_self_bad(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.

    Example 1:
    =================================
        Input: nums = [1,2,3,4]
        Output: [24,12,8,6]
    =================================
    [1,2,3,4]
    ca[24,1, 2, 6]
     

    # note: Go don't index ahead
    ca = [1,1,2,6]
    [24,12,8,6]
    """

    if len(nums) == 1:
        return nums
    copy_nums = [1] * len(nums)
    for outer in range(len(nums)):
        for inner in range(len(nums)): 
            if inner == outer:
                continue
            copy_nums[outer] *= nums[inner] 

    return copy_nums 

def product_except_self_leet(nums):
    ans = [1] * len(nums)
    for i in range(1, len(nums)):
        ans[i] = ans[i-1] * nums[i-1] 
    postfix = 1
    for j in range(len(nums)-1, -1, -1):
        ans[j] *= postfix
        postfix *= nums[j]
    return ans

if __name__ == "__main__":
    input = [1,2,3,4]
    output = [24,12,8,6]

    solutions = [product_except_self_bad, product_except_self_leet]
    for solution in solutions: 
        assert solution(input) == output
