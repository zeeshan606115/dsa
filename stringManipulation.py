import copy
def string_value(user_str):
	s = []
	s1 = []
	l = ''
	for char in user_str:
		s.append(char)
	s1 = s.copy()
	i = 0
	count =1 
	for j in range(1, len(s)):
		if(s[i] == s[j]):
			s1.insert(i+count, '*')
			i = i+1
			count = count+1
		else:
		    i = i+1
	l = ''.join(map(str, s1))  
	print("New String: ",l)
s = input("Enter String: ")
string_value(s)