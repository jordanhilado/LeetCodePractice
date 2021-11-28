# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int]) -> int:
    if prices[::-1] == sorted(prices):
        return 0
    ans = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            ans = max(profit, ans)
        else:
            left = right
        right += 1
    return ans