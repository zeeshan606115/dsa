def max_product(arr):
    prod = 1
    maxProd = float("-inf")
    for i in arr:
        prod *= i
        maxProd = max(prod, maxProd)
        if prod == 0:
            prod = 1
        
    prod  = 1
    i = len(arr) - 1
    while i >=0 :
        prod *= arr[i]
        maxProd = max(prod, maxProd)
        if prod == 0:
            prod = 1
        i -= 1
    return maxProd

print(max_product([8,5,3,1,-6]))
