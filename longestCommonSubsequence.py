def lcs(X,Y):
	T = [[0 for i  in range(10)]for j in range(10)]
	for i in range(len(X)):
		for j in range(len(Y)):
			if (X[i] == Y[j]):
				T[i][j] = 1+T[i-1][j-1]
			else:
				T[i][j] = max(T[i-1][j], T[i][j-1])

	return T[i][j]

X = 'abcdef'
Y = 'pqrbrceuf'
print(lcs(X,Y))