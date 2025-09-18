class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum, count = 0, 0
        prefix_dict = defaultdict(int)
        prefix_dict[0] = 1

        for num in nums:
            sum += num

            if sum - goal in prefix_dict:
                count += prefix_dict[sum - goal]
            
            prefix_dict[sum] += 1

        return count
