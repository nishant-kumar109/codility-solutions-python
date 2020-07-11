
# Brackets
# Determine whether a given string of parentheses (multiple types) is properly nested.


def solution(S):
    valid = True
    stack = []
    for c in S:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)
        elif c == ')':
            valid = False if not stack or stack.pop() != '(' else valid
        elif c == ']':
            valid = False if not stack or stack.pop() != '[' else valid
        elif c == '}':
            valid = False if not stack or stack.pop() != '{' else valid
    return 1 if valid and not stack else 0
		


print(solution("{[()()]}"))
# expected output : 1
print(solution("([)()]"))
# expected output : 0

# codility submited solution link :
# https://app.codility.com/demo/results/trainingCUTDFM-FDB/


