# https://www.geeksforgeeks.org/checking-valid-shuffle-of-two-strings/

'''
    Input: str1 = BA, str2 = XY, shuffle = XYAB 
    Output: YES

    Input: str1 = BA, str2 = XY, shuffle = XUMB 
    Output: NO

    Input: str1 = ABC, str2 = ZYS, shuffle = YBAZSC 
    Output:YES
'''


str1 = 'BA' 
str2 = 'XY'
shuffle = 'XYAB'

# Approach 1 by using sorting the string

# s = str1 + str2
# s = ''.join(sorted(s))
# shuffle = ''.join(sorted(shuffle))
# if s == shuffle:
#     print("valid")
# else:
#     print("Invalid")


# Approarch 2 by using Dictionary
d = {}
for i in str1:
    if d.get(i):
        d[i] += 1
    else:
        d[i] =1
for i in str2:
    if d.get(i):
        d[i] += 1
    else:
        d[i] = 1


for i in range(len(shuffle)):
    if shuffle[i]  in d:
        d[shuffle[i]] -= 1 
    else:
        print("Invalid")
        break
else:
    for key, value in d.items():
        if(value != 0):
            print("Invalid")
            break
    else:
        print("valid")

