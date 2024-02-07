class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        tmp_prices = prices
        for i in range(len(prices)):
            if prices.index(max(prices)) == i:
                
        return max_profit


result = Solution()
test_case = [7,1,5,3,6,4]
print(result.maxProfit(test_case))