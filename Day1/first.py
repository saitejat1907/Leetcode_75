class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#First Attempt: Wrong attempt because i have considered least number in the whole array but need to consider the least number which has greater number in coming days.

        # n = len(prices) - 1
        # least_number = min(prices)
        # b = 0
        # c = prices.index(least_number)
        # for i in range(c, n):
        #     a = prices[i+1] - least_number
        #     if(a>b):
        #         b = a
        # return b

#Second attempt: error as time limit exceeded

        # n = len(prices)
        # b = 0
        # for i in range(n-1):
        #     a = max(prices[i+1:]) - prices[i]
        #     if(a>b):
        #         b = a
        # return b

# third attept: 
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            if (min_price > price):
                min_price = price
            else:
                profit = price - min_price
                if(profit>max_profit):
                    max_profit = profit
        return max_profit