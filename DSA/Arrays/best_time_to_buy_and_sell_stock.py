'''
Problem:You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''
#Approach
'''


Time Complexity:O(n)
Space Complexity:O(1)
'''
#Code
def maxProfit(prices):
    buy=prices[0]
    profit=0
    for i in prices:
        if i<buy:
            buy=i
        profit=max(profit,i-buy)
    return profit 

prices=list(map(int,input("Enter prices :").split(',')))
print(maxProfit(prices))