class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''

        for c in range(len(s)):
            p1 = self.palindrome(s, c, c+1)
            p2 = self.palindrome(s, c, c)
            p = max(p, p1, p2, key=len)

        return p

    def palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
