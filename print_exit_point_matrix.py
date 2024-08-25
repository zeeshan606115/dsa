def print_exit_point(r,c):
    l3 = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        l3.append(row)
    print('-------------')
    l = []
    
    j = 0
    while j <= len(l3[0])-1:
        i = len(l3) - 1
        while i >= 0:   
            print(l3[i][j], end = " ")
            i -= 1
        j += 1
        print()


    direction = 0
    i = 0
    j = 0
    while True:
        direction = (direction+ l3[i][j]) % 4
        if direction == 0:
            j += 1
        elif direction == 1:
            i += 1
        elif direction == 2:
            j -= 1
        elif direction == 3:
            i -= 1
        
        if (i < 0):
            i += 1
            break
        elif (j < 0):
            j += 1
            break
        elif i == len(l3):
            i -= 1
            break
        elif j == len(l3[0]):
            j -= 1
            break
    print(i,j)


print_exit_point(3,3)