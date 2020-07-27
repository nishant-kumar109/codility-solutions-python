# Flags
# Find the maximum number of flags that can be set on mountain peaks

def solution(A):
    # write your code in Python 3.6
    peaks = [0]*len(A)
    next_peak = len(A)
    peaks[len(A) - 1] = next_peak
    
    for i in range(len(A)-2, 0, -1):
        if A[i-1] < A[i] and A[i+1] < A[i]:
            next_peak = i
        peaks[i] = next_peak
    peaks[0] = next_peak
    
    current_guess = 0
    next_guess = 0
    while can_place_flags(peaks, next_guess):
        current_guess = next_guess
        next_guess+=1
    return current_guess
    
def can_place_flags(peaks, flags_to_place):
    current_position = 1 - flags_to_place
    for i in range(flags_to_place):
        if current_position + flags_to_place > len(peaks) -1:
            return False
        current_position = peaks[current_position + flags_to_place]
    return current_position < len(peaks)


print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))

# expected output : 3
# submitted solution link : 
# https://app.codility.com/demo/results/trainingYK3YRA-8A4/