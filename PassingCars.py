
#  PassingCars
# Count the number of passing cars on the road.

def solution(A):
    # write your code in Python 3.6
    suffix_sum = [0]*(len(A) + 1)
    for i in range(len(A) - 1, -1, -1):
        suffix_sum[i] = A[i] + suffix_sum[i+1]
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count+=suffix_sum[i]
        if count > 1000000000:
            return -1
    return count

print(solution([0,1,0,1,1]))

# expected output : 5
# submitted solution link : 
# https://app.codility.com/demo/results/trainingHM7Q3M-WA5/