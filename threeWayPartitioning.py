##### https://practice.geeksforgeeks.org/problems/three-way-partitioning/1#

def threePart(arr, a, b, n):
    start = 0
    end = n - 1
    i = 0
    while i <= end:
        if arr[i] < a:
            arr[i], arr[start] = arr[start], arr[i]
            i += 1
            start += 1
        elif arr[i] > b:
            arr[i], arr[end] = arr[end], arr[i]
            end -= 1
        else:
            i += 1
    
    return arr
a = [1,2,3,3,4]
n = 5
print(threePart(a, 1,2, 5))