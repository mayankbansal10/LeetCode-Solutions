class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0

        for num in nums:

            currSum += num
            if currSum > maxSum:
                maxSum = currSum

            if currSum < 0:
                currSum = 0

        return maxSum
