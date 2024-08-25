# arr = [5,7,4,3,9,8,19,21]
# sum = 17

def sumPair(arr, sum):
	arr.sort()
	left = 0
	right = len(arr)-1
	count  = 0
	while (left<=right):
		if(arr[left] + arr[right] > sum):
			right = right - 1
		elif(arr[left] + arr[right] < sum):
			left = left + 1
		elif(arr[left] + arr[right] == sum):
			print("value of Piar are: ",arr[left]," and ", arr[right])
			right = right - 1
			left = left + 1
			count = count + 1
	return count


arr = [5,7,4,3,9,8,19,21]		
sum = 17
x = sumPair(arr, sum)
if x == 0:
	print("Not possible")