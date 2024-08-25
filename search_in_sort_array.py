def search_array(arr, x):
    i = 0
    j = len(arr[0]) - 1 
    while (i < len(arr) and j >= 0):
        if (x == arr[i][j]):
            print(i,j)
            return
        elif(x < arr[i][j]):
            j -= 1
        else:
            i += 1
    print("Element Not found")
    return


arr = [[11, 12, 13, 14, 15, 16],
[21, 22, 23, 24, 25, 26],
[31, 32, 33, 34, 35, 36],
[41, 42, 43, 44, 45, 46]
]
search_array(arr, 45)