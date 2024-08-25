def lsc(x):
    length = len(x)
    T= []
    # T = [[0 for i  in range(length)]for j in range(length)]
    for i in range(length):
        for j in range(length):
            T[i][j]=0
    print(T)
lsc('asdasdas')