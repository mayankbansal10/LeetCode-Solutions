class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = 0
        sum_n = sum(nums)

        for i in range(len(nums)):
            sum_n -= nums[i]
            if sum_n == res:
                return i
            res += nums[i]
        
        return -1
