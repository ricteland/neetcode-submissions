class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        bestprofit = -math.inf
        L = 0

        for R in range(len(prices)):

            profit = prices[R] - prices[L]

            bestprofit = max(bestprofit, profit)

            if profit < 0:

                L = R
                
        return bestprofit