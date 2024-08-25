# https://leetcode.com/problems/minimum-size-subarray-sum/description/

'''
    Given an array of positive integers nums and a positive integer target, return the minimal length of a 
    subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

    Example 1:

    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem constraint.
    Example 2:

    Input: target = 4, nums = [1,4,4]
    Output: 1
    Example 3:

    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0
'''


class Solution:
    def minSubArrayLen(self, target, nums):
        i = j = sum = 0
        min_l = float('inf')

        while j < len(nums):

            sum += nums[j]
            #  Here we are decreasing the window size
            while sum >= target:
                min_l = min(min_l,j - i + 1)
                sum -= nums[i]
                i += 1 

                

            j += 1 
        if min_l == float('inf'):
            return 0 
        return min_l

nums = [1,1,1,1,1,1,1,1]
target = 11
ob = Solution()
result = ob.minSubArrayLen(target, nums)
print(result)