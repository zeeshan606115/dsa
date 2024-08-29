class Solution:

    def firstNegative(self, nums, k, n):
        result = []
        deq = []
        i = j = 0
        while j < n:
            if nums[j] < 0:
                deq.append(nums[j])

            if (j - i + 1 == k):
                if len(deq) != 0:
                    result.append(deq[0])
                else:
                    result.append(0)
                
                if nums[i] < 0 and len(deq) > 0:
                    deq.pop(0)
                i += 1 
            j += 1 

        return result


nums = [-8,2,3,-6,10]
k = 2
n = len(nums)
ob = Solution()
res = ob.firstNegative(nums, k, n)
print(res)