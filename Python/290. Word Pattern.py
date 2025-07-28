class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.strip().split(" ")

        if len(words) != len(pattern):
            return False

        p2w,w2p = {}, {}

        for c, w in zip(pattern, words):
            if  (c in p2w and p2w[c] != w) or (w in w2p and w2p[w] != c):
                return False
            p2w[c] = w
            w2p[w] = c
        
        return True
