# Topics: Array, TwoPointers, Sliding-Window, DynamicProgramming

# BruteForce Approach
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res

# Optimized Approach
class Solution2:
    def maxProfit(self, prices):
        l, r = 0, 1 # Left(l) = Buy, Right(r) = Sell
        maxProfit = 0

        while r < len(prices):
            # is it profitable to sell?
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(currentProfit, maxProfit)

            else:
                l = r # we find lowest price for shares here
            r += 1

        return maxProfit