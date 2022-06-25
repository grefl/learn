
def maxProfit(prices):
    profit = 0
    i = 0
    curr_min = 10**20
    while i < len(prices):
        if curr_min > prices[i]:
            curr_min = prices[i]
        elif curr_min < prices[i]:
            profit = max(prices[i] - curr_min, profit)
        i +=1
    return profit



if __name__ == "__main__":
     prices = [0,2,4,3,1] 
     profit = maxProfit(prices)
     print(profit)
