def rearrange(arr):
    arr.sort(reverse = True)
    print(arr)
    j = float("-inf")
    for i in range(len(arr)):
        if arr[i] < 0:
            j = i
            break
    k = j
    i = 0
    for j in range(k,len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
        i += 2  
    print(arr)

rearrange([2,3,-5,-4,1,6,-5])