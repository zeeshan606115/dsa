def arraySubset(arr1, arr2):
    for i in arr2:
        if i in arr1:
            pass
        else:
            print("Not Possible")
            break
    else:
        print("Possible")


a1 = [11, 1, 13, 21, 3, 7]
a2 = [11, 3, 7, 1,90]
arraySubset(a1, a2)