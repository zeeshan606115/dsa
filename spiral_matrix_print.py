def spiral_matrix(r,c):
    l3 = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        l3.append(row)

    minr = 0
    minc = 0
    maxr = len(l3) - 1
    maxc = len(l3[0]) - 1

    tne =  r * c
    cnt = 0
    while cnt < tne:
        i = minr
        j = minc
        while(i <= maxr and cnt < tne):
            print(l3[i][j], end = " ")
            i += 1
            cnt += 1
        minc += 1
        i = maxr
        j = minc
        while (j<= maxc and cnt < tne):
            print(l3[i][j], end = " ")
            j += 1
            cnt += 1
        maxr -= 1
        i = maxr
        j = maxc
        while i >= minr and cnt < tne:
            print(l3[i][j], end = " ")
            i -= 1
            cnt += 1
        maxc -= 1
        i = minr
        j = maxc
        while (j >= minc and cnt < tne):
            print(l3[i][j], end = " ")
            j -= 1
            cnt += 1
        minr += 1
        print()

spiral_matrix(5,5)