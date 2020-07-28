

# CountDistinctSlices
# Count the number of distinct slices (containing only unique numbers).

def solution(M, A):
    # write your code in Python 3.6
    total_slice = 0
    in_current_slice = [False]*(M+1)
    head = 0
    for tail in range(0, len(A)):
        while head<len(A) and (not in_current_slice[A[head]]):
            in_current_slice[A[head]] = True
            total_slice += (head-tail) + 1
            head +=1
            total_slice = 1000000000 if total_slice > 1000000000 else total_slice
        in_current_slice[A[tail]] = False
    return total_slice


print(solution(6, [3, 4, 5, 5, 2]))
# expected output : 9
# submitted solution link : 
# https://app.codility.com/demo/results/trainingRT7BKP-Z3W/