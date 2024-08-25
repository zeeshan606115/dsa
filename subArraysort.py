def subArraySort(array):
	minOutOfOrder = float("inf")
	maxOutOfOrder = float("-inf")
	if len(array) == 1:
		return "No swap possible"
	for i in range(len(array)):
		num = array[i]
		if isOutOfOrder(i, num, array):
			minOutOfOrder = min(minOutOfOrder, num)
			maxOutOfOrder= max(maxOutOfOrder, num)
	if minOutOfOrder == float("inf"):
		return "No swap possible"
	subarrayLeftIdx = 0
	while minOutOfOrder >= array[subarrayLeftIdx]:
		subarrayLeftIdx +=1
	subarrayRightIdx = len(array)- 1

	while maxOutOfOrder <= array[subarrayRightIdx]:
		subarrayRightIdx -= 1
	return [subarrayLeftIdx, subarrayRightIdx]

def isOutOfOrder(i, num, array):
	if i == 0:
		return num > array[i + 1]
	if i == len(array) - 1:
		return num < array[i-1]
	return num > array[i + 1] or num < array[i-1]

print(subArraySort([1,2,3,7,6,5,9,10,11]))
print(subArraySort([1,2,3,7,6,5,-1]))
print(subArraySort([1]))
print(subArraySort([1,2,3,4,5,6]))
print(subArraySort([]))