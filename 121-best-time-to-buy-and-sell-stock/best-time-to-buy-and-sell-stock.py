class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_p = max(max_p, profit)
            else:
                left = right 
            right += 1
        return max_p


