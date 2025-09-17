class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        sum = 0
        prefix_sum_dict = {0:1}

        for num in nums:
            sum += num
            mod = sum % k
            if mod < 0:
                mod += k
            if mod in prefix_sum_dict:
                count += prefix_sum_dict[mod]
                prefix_sum_dict[mod] += 1
            else:
                prefix_sum_dict[mod] = 1
        
        return count
