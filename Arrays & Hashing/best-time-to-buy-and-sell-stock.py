class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        profit = 0
        for val in prices: 
            mini = min(mini,val) 
            profit = max(profit, val - mini)
        return profit
    
# This problem givs us a list of integers which represents the price of a certain stock on that day.
# It asks us to find the best time to buy and sell the stock which means the finding the maximum profit 
# possible. To do this, I had a variable that stores the smallest value we have seen so far and a profit
# variable that stored the greatest profit we have seen so far. After one loop we should have the maximum profit.