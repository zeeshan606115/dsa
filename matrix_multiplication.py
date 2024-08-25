def matrix_multiply(R1,C1,R2,C2):
    if (C1 != R2):
        print("Array not possible")
        return
    l = []
    for i in range(R1):
        row = []
        for j in range(C1):
            row.append(int(input()))
        l.append(row)

    l2 = []
    for i in range(R2):
        row = []
        for j in range(C2):
            row.append(int(input()))
        l2.append(row)
    
    l3 = [ [0]*R2 for i in range(C2)]
    print(l3)
    for i in range(len(l3)):
        for j  in range(len(l3[0])):
            for k in range(C1):
                l3[i][j] += l[i][k] + l2[k][j]
    
    print(l3)
    
matrix_multiply(3,3,3,3)