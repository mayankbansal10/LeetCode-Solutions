class Solution:
    def countPalindromes(self, l, r, s):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1

        return count

    def countSubstrings(self, s: str) -> int:
        return sum(self.countPalindromes(i, i, s) + self.countPalindromes(i, i+1, s) for i in range(len(s)))
