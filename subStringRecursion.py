def isSubString(str1, str2):
	size1 = len(str1)
	size2 = len(str2)
	if (size1 == 0 and size2 == 0):
		print('issub')
		return True
	if (size1 == 0):
		return False

	if(size2 == 0):
		return True

	if(str1[0] == str2[0]):
		return ExactSame(str1,str2)
	return isSubString(str1[1:], str2)

def ExactSame(str1, str2):
	size1 = len(str1)
	print("size1: ",size1)
	
	size2 = len(str2)
	print("size2: ",size2)
	if (size1 == 0 and size2 == 0):
		return True
	if (size1 == 0):
		return False
	if(size2 == 0):
		return True
	if(str1[0] == str2[0]):
		return ExactSame(str1[1:], str2[1:])
	print("dkjfn")
	return False

str1 = "ZEESHAN"
str2 = 'HAN'
p = isSubString(str1, str2)
print(p)