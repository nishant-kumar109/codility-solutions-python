# cyclic rotaion

# Rotate an array to the right by a given number of steps.

def solution(A,K):
	result = [None]*len(A)
	for i in range(len(A)):
		result[(i+K)%len(A)] = A[i]
	return result


print(solution([3, 8, 9, 7, 6], 3))




# expected output : [9, 7, 6, 3, 8]
# submitted solution link :
# https://app.codility.com/demo/results/trainingSDZXJT-KQA/