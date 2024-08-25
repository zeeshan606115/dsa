# An array is called equilibruim array when left sum of array must be equal to right sum

arr = [-7, 1, 5, 2, -4, 3, 0]
def fun():
    lftSum = 0
    tSum = sum(arr)
    for i in range(len(arr)):
        tSum -= arr[i]
        if lftSum == tSum:
            return i
        else:
            lftSum += arr[i]
    return -1

x = fun()
print(x)
