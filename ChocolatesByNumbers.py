# ChocolatesByNumbers
# There are N chocolates in a circle. Count the number of chocolates you will eat.

def find_gcd(a,b):
    if b==0:
        return a
    else:
        return find_gcd(b, a%b)
        
        
def solution(N, M):
    # write your code in Python 3.6
    return N//find_gcd(N,M)


print(solution(10,4))


# expected output : 5
# submitted solution link : 
# https://app.codility.com/demo/results/trainingV94GBF-4DU/