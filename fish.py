
# problem statement
# N voracious fish are moving along a river. Calculate how many fish are alive.

def solution(A, B):
    # write your code in Python 3.6
    stack = []
    surviver = 0
    
    for i in range(len(A)):
        weight = A[i]
        if B[i] == 1:
            stack.append(weight)
        else:
            weightDown = stack.pop() if stack else -1
            while weightDown != -1 and weightDown < weight:
                weightDown = stack.pop() if stack else -1
            if weightDown == -1:
                surviver+=1
            else:
                stack.append(weightDown)
    return surviver + len(stack)

print(solution([4,3,2,1,5], [0,1,0,0,0]))




# submitted solution
# https://app.codility.com/demo/results/trainingBCGAWT-7GE/