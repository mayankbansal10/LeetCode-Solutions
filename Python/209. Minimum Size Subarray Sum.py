class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, n, sum = 0, len(nums), 0
        min_len = float('inf')
        for r in range(n):
            sum += nums[r]

            while sum >= target:
                min_len = min(min_len, r - l + 1)
                if min_len == 1:
                    return min_len
                sum -= nums[l]
                l += 1

        return 0 if min_len == float('inf') else min_len

        
