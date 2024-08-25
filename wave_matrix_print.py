def wave_print(r,c):
    l3 = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        l3.append(row)
    
    print()
    print('------------------------')



    for j in range(len(l3[0])):
        if j % 2 == 0:
            for i in range(len(l3)):
                print(l3[i][j])
        else:
            i = len(l3) -1
            while i >= 0:
                print(l3[i][j])
                i -= 1


wave_print(3,3)