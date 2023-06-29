class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        while right < len(prices):
            cur_profit = prices[right] - prices[left]
            if prices[right]>prices[left]:
                profit = max(cur_profit,profit)
            else:
                left = right
            right+=1
        return profit
