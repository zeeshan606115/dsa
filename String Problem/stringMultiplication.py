m = '0'
n = '456'

def multiplication_string(n,m):
    if m == '0' or n =='0' or len(m) == 0 or len(n) == 0:
        return 0
    if m =='1':
        return n
    if n == '1':
        return m
    result = [0] * len(m + n)
    
    for i in range(len(m) - 1, -1, -1):
        for j in range(len(n) - 1, -1, -1):
            product = int(m[i]) * int(n[j])
            product += result[i + j + 1]
            result[i + j + 1] = product % 10 
            result[i + j] += product // 10 
    if result[0] == 0:
        result=result[1:]
    result = result
    result = ''.join(str(i) for i in result)
    return result

s = multiplication_string(m,n)
print(s)
