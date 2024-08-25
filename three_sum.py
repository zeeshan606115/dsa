def threeSum(lst):
 	res =[]
 	lst.sort()
 	length = len(lst)

 	for i in range(length-2):
 		if i> 0 and lst[i] == lst[i-1]:
 			continue
 		l =i + 1
 		r = length-1
 		while l < r:
 			total = lst[i] + lst[l] +lst[r]
 			
 			if total < 0:
 				l += 1
 			elif total > 0:
 				r = r - 1
 			else:
 				print(lst[i], lst[l], lst[r])
 				while l<r and lst[l] == lst[l+1]:
 					l +=1
 				while l<r and lst[r] == lst[r-1]:
 					r -= 1
 				l = l+1
 				r = r-1

l = [-1,-4,5,2,0,1,-3]
threeSum(l)