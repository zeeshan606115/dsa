def hamming_dist(x,y):
	count = 0
	sol = x^y
	for i in range(32):
		if(sol>>i) & 1 == 1:
			count = count + 1

	return count

print(hamming_dist(1,6))