def shell_reverse(arr, s, r):
    oned = fillOnedFromShell(arr, s)
    rotate(oned, r)
    fillShellFromOned(arr, s, oned)
    print(arr)
    print("888888888888888888888")
    print("-------------------------")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
    
def fillShellFromOned(arr, s, oned):
    minr = s-1
    minc = s - 1
    maxr = len(arr) - s
    maxc = len(arr[0]) - s

    # Left wall filling

    idx = 0
    j = minc
    i = minr
    while i <= maxr:
        arr[i][j] = oned[idx]
        idx +=1
        i += 1
    
    # Bottom wall filling
    i = maxr
    j = minc + 1
    while j <= maxc:
        arr[i][j] = oned[idx]
        idx += 1
        j += 1

    # Right wall filling
    j = maxc
    i = maxr -1
    while i >= minr:
        arr[i][j] = oned[idx]
        idx +=1
        i -= 1

    # Top wall filling
    i = minr
    j = maxc - 1
    while j >= minc + 1:
        arr[i][j] = oned[idx]
        idx += 1
        j -= 1
    
    return arr


def fillOnedFromShell(arr, s):
    minr = s-1
    minc = s - 1
    maxr = len(arr) - s
    maxc = len(arr[0]) - s
    sz = 2 * (maxr - minr + maxc - minc)
    oned = [0] * sz

    # Left wall filling

    idx = 0
    j = minc
    i = minr
    while i <= maxr:
        oned[idx] = arr[i][j]
        idx +=1
        i += 1
    
    # Bottom wall filling
    i = maxr
    j = minc + 1
    while j <= maxc:
        oned[idx] = arr[i][j]
        idx += 1
        j += 1

    # Right wall filling
    j = maxc
    i = maxr -1
    while i >= minr:
        oned[idx] = arr[i][j]
        idx +=1
        i -= 1

    # Top wall filling
    i = minr
    j = maxc - 1
    while j >= minc + 1:
        oned[idx] = arr[i][j]
        idx += 1
        j -= 1
    
    return oned

    

def rotate(oned, r):
    r = r % len(oned)
    if(r < 0):
        r = r + len(oned)

    reverse(oned, 0, len(oned) - r - 1)
    reverse(oned, len(oned) - r, len(oned) - 1)
    reverse(oned, 0, len(oned) - 1)


def reverse(oned, li, ri):
    while(li < ri):
        oned[li], oned[ri] = oned[ri], oned[li]
        li += 1
        ri -= 1

arr = [[11, 12, 13, 14, 15, 16],
[21, 22, 23, 24, 25, 26],
[31, 32, 33, 34, 35, 36],
[41, 42, 43, 44, 45, 46],
[51, 52, 53, 54, 55, 56],
[61, 62, 63, 64, 65, 66]
]

shell_reverse(arr,1,6)