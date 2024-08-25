def get_saddle_point(arr):
    for i in range(len(arr)):
        svj = 0
        for j in range(1, len(arr[0])):
            if arr[i][j] < arr[i][svj]:
                svj = j
        flag = True
        for k in range(len(arr)):
            if arr[k][svj] > arr[i][svj]:
                flag = False
                break

        if flag == True:
            print(arr[i][svj]) 
            return
    print("Invalid Input")


arr = [[11, 12, 13, 14, 15, 16],
[21, 22, 23, 24, 25, 26],
[31, 32, 33, 34, 35, 36],
[41, 42, 43, 44, 45, 46]
]
get_saddle_point(arr)