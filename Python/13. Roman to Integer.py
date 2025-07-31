class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        ans = 0
        for i in range(len(s)):
            curr = mapping[s[i]]
            next = mapping[s[i+1]] if i + 1 < len(s) else 0

            if curr < next:
                ans -= curr
            else:
                ans += curr
        
        return ans
