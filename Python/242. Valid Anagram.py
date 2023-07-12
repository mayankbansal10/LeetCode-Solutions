from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)
        ans = True
        for i in range(len(s)):
            if s_counter[s[i]] != t_counter[s[i]]:
                ans = False

        return ans
