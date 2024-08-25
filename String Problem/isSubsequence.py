def checkSubsequence(s,t):
    m = len(s)
    n = len(t)
    i = j = 0
    while (i <m and j < n):
        if (s[i] == t[j]):
            i += 1 
        j += 1 
    if i == m:
        return True
    return False

res= checkSubsequence('abx', 'acdbdsc')
print(res)