def repeatString(s):
    n = len(s)
    res = ''
    for i in range(1,n):
        if (n % i == 0):
            res = s[0:i]* (n//i )
            if res == s:
                return True
    return False
s = repeatString('abcd')
print(s)