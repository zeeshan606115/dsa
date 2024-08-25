l = [2,7,11, 11, 15, 20]
sum = 22
mylist = [(values, index) for index, values in enumerate(l)]
mylist.sort()
begin = 0
end = len(mylist)-1

while begin < end:
	target = mylist[begin][0] + mylist[end][0]
	if target == sum:
		print(mylist[begin][0],mylist[end][0])
		end = end-1
		
	elif target > sum:
		end = end-1
		
	elif target < sum:
		begin = begin + 1
	else:
		print('not found')
