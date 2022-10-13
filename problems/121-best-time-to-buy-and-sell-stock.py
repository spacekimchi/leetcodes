class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        cur = 0
        pre = prices[0]
        for i, price in enumerate(prices):
            cur += price - pre
            pre = price
            ans = max(ans, cur)
            if cur < 0:
                cur = 0
        return ans

