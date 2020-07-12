
# Dominator
# Find an index of an array such that its value occurs at more than half of indices in the array.

def solution(A):
    consecutive_size = 0
    candidate = 0
    for item in A:
        if consecutive_size == 0:
            candidate = item
            consecutive_size+=1
        elif candidate == item:
            consecutive_size+=1
        else:
            consecutive_size-=1
    occurance = A.count(candidate)
    if occurance > (len(A)/2):
        return A.index(candidate)
    else:
        return -1

print(solution([3,4,3,2,3,-1,3,3]))

# expected output : 0 (index of first occurance of 3)
# submitted solution link:
# https://app.codility.com/demo/results/trainingBBKVVE-ERV/ 
