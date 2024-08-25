def minJumps(arr):
	if arr[0] == 0:
		return float('inf')
	end = len(arr)

	dp = [0 for i in range(end)]
	for i in range(1, end):
		dp[i] = float('inf')
		for j in range(0,i):
			if i <= j + arr[j]:
				dp[i] = min(dp[i], dp[j] + 1)
	return dp[-1]
lst = [2,3,1,1,4]
print(minJumps(lst))