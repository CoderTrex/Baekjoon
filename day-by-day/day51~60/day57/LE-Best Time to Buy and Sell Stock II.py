from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import collections
        prices = collections.deque(prices)
        profit = 0
        buy = prices.popleft()
        while prices:
            sell = prices.popleft()
            if sell > buy:
                profit += (sell - buy)
            buy = sell
        return profit