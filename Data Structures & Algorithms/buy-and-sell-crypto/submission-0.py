class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bestprofit = -math.inf
        curL, curR = 0, 1

        L = 0

        for R in range(len(prices)):

            profit = prices[R] - prices[L]

            if profit > bestprofit:

                bestprofit = profit

            if profit < 0:

                L = R
                
        return bestprofit