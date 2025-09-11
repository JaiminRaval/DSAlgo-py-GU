class Solution(object):
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
