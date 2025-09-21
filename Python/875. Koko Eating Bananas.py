class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (l + r) // 2
            hours = sum((p + m - 1)// m for p in piles)

            if hours <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
