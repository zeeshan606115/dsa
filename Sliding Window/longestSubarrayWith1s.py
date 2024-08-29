# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

'''
APPROACH:- 
    We are iterating over list and if we found the current element of list in zero then we are storing the 
    last seen 0 index + 1 to i and
    we are replacing the last seen zero with found zero.
    In each iteration we are compaing the result value and updating it.
'''

class Solution:
    
    def longestSubarray(self, nums):
        i = j = 0
        ar_len = len(nums)
        result = 0
        last_zero = -1
        while j < ar_len:
            if nums[j] == 0:
                i = last_zero + 1
                last_zero = j
            result = max(result, j-i)
            j += 1
            
        return result


nums = [1,1,1]
obj = Solution()
res = obj.longestSubarray(nums)
print(res)