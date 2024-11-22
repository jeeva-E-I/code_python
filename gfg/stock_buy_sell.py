#STOCK BUY AND SELL PROGRAM [MULTIPLE TRANSACTIONS ARE ALLOWED]
prices = [4, 2, 2, 2, 4]
def maximumProfit(prices) -> int:
    profit = 0
    total_profit = 0
    i = 0    
    while  i < len(prices)-1:
        if prices[i] < prices[i+1]:
            buy = prices[i]
            for j in range(i,len(prices)-1):
                if prices[j] > prices[j+1]:
                    selling_value = prices[j]
                    profit = selling_value - buy
                    i = j+1
                    total_profit = total_profit + profit
                    break
                elif j == len(prices)-2:
                    selling_value = prices[j+1]
                    profit = selling_value - buy
                    total_profit = total_profit + profit
                    i = j+1
        else:
            i = i+1
        
    return total_profit


print(maximumProfit(prices))