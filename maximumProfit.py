
# MaxProfit
# Given a log of stock prices compute the maximum possible earning.

def solution(A):
    global_max_sum = 0
    local_max_sum = 0
    for i in range(1, len(A)):
        d = A[i] - A[i-1]
        local_max_sum = max(d, local_max_sum + d)
        global_max_sum = max(local_max_sum, global_max_sum)
    return global_max_sum




print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

# expected output : 356 
# submitted solution link:
# https://app.codility.com/demo/results/trainingX6CPAN-HXQ/