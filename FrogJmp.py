# FrogJmp
# Count minimal number of jumps from position X to Y.

def solution(X, Y, D):
    # write your code in Python 3.6
    distance_to_jump = Y-X
    if distance_to_jump % D == 0:
        return distance_to_jump//D
    else:
        return (distance_to_jump//D) +1


print(solution(10,85,30))

# expected out put : 3

# submitted solution link:
# https://app.codility.com/demo/results/training73EP89-QWX/