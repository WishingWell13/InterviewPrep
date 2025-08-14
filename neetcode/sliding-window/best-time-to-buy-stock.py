'''
https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150

Input: prices = [10,1,5,6,7,1]
                b   b       e
Output: 6
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        sellDay = 0 #inclusive
        bestProfit = 0


        while sellDay < len(prices):
            if prices[sellDay] < prices[buyDay]:
                buyDay = sellDay

            bestProfit = max(prices[sellDay] - prices[buyDay], bestProfit)
            sellDay += 1

        return bestProfit
