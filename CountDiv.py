
#  CountDiv
# Compute number of integers divisible by k in range [a..b].


from math import ceil, floor 
def solution(A, B, K):
    # write your code in Python 3.6
    n_start = ceil(A/K)
    n_end = floor(B/K)
    return n_end - n_start + 1

print(solution(6, 11, 2))
# expected output : 3
# submitted solution link : 
# https://app.codility.com/demo/results/trainingCT763E-T9V/