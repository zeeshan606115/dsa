def rev_digit(str):
	size = len(str)
	if(size == 0):
		return 

	else:
		last_char = str[size-1]
		if (last_char.isdigit()):
			print(last_char, end="")
		rev_digit( str[0:size-1])
rev_digit('s34b5a1')