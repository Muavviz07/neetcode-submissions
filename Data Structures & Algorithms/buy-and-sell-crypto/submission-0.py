class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0
        buy = prices[0]
        sell = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            sell = max(sell, prices[i] - buy)
            
        return sell