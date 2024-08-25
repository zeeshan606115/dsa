term = [0 for i in range(100)]
def fib(n):
    if n <= 1:
        return 1
    
    if (term[n] != 0):
        return term[n]
    else:
        term[n] = fib(n-1) + fib(n-2)
        return term[n]
    
print(fib(5))
    