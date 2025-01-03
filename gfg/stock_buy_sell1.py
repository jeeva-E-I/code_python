# STOCK BUY AND SELL PROGRAM [SINGLE BUY AND SELL]
def maximumProfit(self, prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit,profit)
        min_price = min(min_price,price)
    return max_profit