class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freqMap = {}
        majority = [-1,-1]
        for num in nums:
            if num in freqMap:
                freqMap[num] += freqMap[num]+1                
            else:
                freqMap[num] = 1
            if freqMap[num] > majority[1]:
                    majority[0] = num
                    majority[1] = freqMap[num]

        return majority[0]
