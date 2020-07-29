# TieRopes
# Tie adjacent ropes to achieve the maximum number of ropes of length >= K.

def solution(K, A):
    # write your code in Python 3.6
    count = 0
    rope_length = 0
    for rope in A:
        rope_length += rope
        if rope_length >= K:
            count+=1
            rope_length = 0
    return count

print(solution(4, [1, 2, 3, 4, 1, 1, 3]))


# expected output : 3
# submitted solution link:
# https://app.codility.com/demo/results/trainingXTP8V7-7ZE/