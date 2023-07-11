class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freqDict = defaultdict(int)
        max_len = 0
        max_freq = 0

        while r < len(s):
            freqDict[s[r]] += 1

            max_freq = max(max_freq, freqDict[s[r]])

            if ((r - l + 1) - max_freq) > k:
                freqDict[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len
