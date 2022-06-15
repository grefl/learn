

class Solution:
    def findMaxAverage(self, nums):
        """
        You are given an integer array nums consisting of n elements, and an integer k.
        Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


        Example 1:
        =======================================================================
        Input: nums = [1,12,-5,-6,50,3], k = 4
        Output: 12.75000
        Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
        =======================================================================

        """

        left = 1 
        right = k
        max_sum = sum(nums[:k])
        print(max_sum)
        current_sum = max_sum 
        while right  < len(nums):
            current_sum = current_sum - nums[left-1] + nums[right]

            max_sum = max(max_sum,current_sum)
            left +=1
            right +=1
            

        return max_sum / k 
    



if __name__ == "__main__":

    nums = [1,12,-5,-6,50,3]
    k = 4 
    solution = Solution()
    res = solution.findMaxAverage(nums)
    print(res)
