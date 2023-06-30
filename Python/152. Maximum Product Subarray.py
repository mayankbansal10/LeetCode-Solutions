class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = maxProd = minProd = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], maxProd * nums[i], minProd * nums[i])
            minProd = min(nums[i], maxProd * nums[i], minProd * nums[i])
            maxProd = temp
            res = max(maxProd, res)

        return res
