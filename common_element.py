def common_in_sorted(a1, a2, a3, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    ans = []
    prev1 = prev2 = prev3 = float('-inf')
    while (i < n1 and j <n2 and k < n3):
        while (a1[i] == prev1 and i < n1):
            i += 1
        while (a2[j] == prev2 and j < n2):
            j += 1
        while (a3[k] == prev2 and k < n3):
            k += 1

        if (a1[i] == a2[j] and a2[j] == a3[k]):
            ans.append(a1[i])
            prev1 = a1[i]
            prev2 = a2[j]
            prev3 = a3[k]
            i += 1
            j += 1
            k += 1
        elif(a1[i] < a2[j]):
            prev1 = a1[i]
            i += 1
        elif(a2[j] < a3[k]):
            prev2 = a2[j]
        else:
            prev3 = a3[k]
            k += 1
    
    return ans


a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = 6
n2 = 5
n3 = 8
print(common_in_sorted(a1,a2,a3,n1,n2,n3))