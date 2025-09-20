class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        while l < r:
            m = ( l + r ) // 2

            cur_weight, days_needed = 0, 1
            for w in weights: 
                if cur_weight + w > m:
                    days_needed += 1
                    cur_weight = 0
                cur_weight += w
            
            if days_needed > days:
                l = m + 1
            else:
                r = m
        
        return l
