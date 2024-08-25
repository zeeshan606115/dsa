def sell_stock(prices, n):
    maxRight = prices[n-1]
    maxProfit = 0
    i = n-2
    while i >= 0:
        maxRight = max(prices[i], maxRight)
        maxProfit = max(maxProfit, maxRight - prices[i])
        i -= 1
    return maxProfit

arr = [7, 1, 5, 3, 6, 14]
print(sell_stock(arr, 6))
