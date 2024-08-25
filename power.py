def get_power(number, power):
	res =1
	for i in range(power):
		res *= number
		# res = res * number
	print(res)
get_power(3,3)

d1={"mango": "fruit", "apple": "fruit", "carrot": "vegetables", "tomato": "vegetables"}
d2 = {}
#d2 = {"fruit": ["mango", "apple"], "vegetables": ["carrot", "tomato"]}
for key, value in d1.items():
	if value not in d2:
		d2[value] = [key]
	else:
		d2[value].append(key)
print(d2)

# l = [1,1,1,2,1,1,3,3,3]
# d = {}
# for i in range(len(l)):
# 	if l[i] not in d:
# 		d[l[i]] = 1
# 	else:
# 		d[l[i]] += 1
# for key, value in d.items():
# 	if value == 1:
# 		print(key)

l = [0,1,1,2,3, 5,8]

def fibbonacci(num):
	a, b = 0,1
	for i in range(0, num):
		c = a + b 
		if c < num:
			# l.append(c)
			yield c

			a, b = b, c

		
print(fibbonacci(10))




	# for j in range(i+1,len(l)):
	# 	if l[i] == l[j]:
	# 		break
	# 	else:
	# 		pass
	# else:
	# 	print(l[i])
	# print(j)
	# if j == len(l):
	# 	print(l[j])