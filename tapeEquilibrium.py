
# TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.


def solution(A):
    # write your code in Python 3.6
    left_sum = A[0]
    right_sum = sum(A) - A[0]
    diff = abs(left_sum - right_sum)
    
    for i in range(1, len(A) - 1):
        left_sum += A[i]
        right_sum -= A[i]
        current_diff = abs(left_sum - right_sum)
        
        if current_diff < diff:
            diff = current_diff
        
    return diff


print(solution([3,1,2,4,3]))

# submitted solution link
#https://app.codility.com/demo/results/trainingH2PSXP-JC9/