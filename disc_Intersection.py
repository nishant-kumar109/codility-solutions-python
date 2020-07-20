 
 # NumberOfDiscIntersections
 # Compute the number of intersections in a sequence of discs.


class DiscLog():
	def __init__(self, x, start_end):
		self.x= x
		self.start_end = start_end
    
def solution(A):
    discHistory = []
    for i in range(len(A)):
        discHistory.append(DiscLog(i - A[i], 1))
        discHistory.append(DiscLog(i + A[i], -1))
    discHistory.sort(key = lambda d: (d.x, -d.start_end))
    intersections = 0
    active_intersections = 0
    for log in discHistory:
        active_intersections += log.start_end
        if log.start_end > 0:
            intersections += active_intersections -1
        if intersections > 10000000:
            return -1
    return intersections





print(solution([1, 5, 2, 1, 4, 0]))

# expected output : 11 
# submitted solution link:
# https://app.codility.com/demo/results/trainingESZXJY-AGS/