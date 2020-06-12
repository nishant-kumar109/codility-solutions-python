
# MaxProfit

# Given a log of stock prices compute the maximum possible earning.

# bassed on Kadden's Algorith

def solution(A):
	global_max_diff = 0
	local_max_diff = 0
	for i in range(1,len(A)):
		delta = A[i] - A[i-1]

		local_max_diff = max(delta, local_max_diff + delta)

		global_max_diff = max(local_max_diff, global_max_diff)

	return global_max_diff
		
print(solution([23171, 21011 ,21123, 21366 ,21013, 21367]))

# codility solution link : 
# https://app.codility.com/demo/results/trainingAPVCM7-XFS/