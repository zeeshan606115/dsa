def trailing_zeros(num):
	oc = 5
	count = 0
	while (num / oc >= 1):
		count += num// oc
		oc = oc *5
	return count
num = int(input('Enter Number: '))
x  = trailing_zeros(num)
print('Traling zero in factorial {} is {} '.format(num, x))