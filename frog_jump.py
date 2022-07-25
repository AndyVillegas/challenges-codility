# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    delta = Y - X
    steps = delta / D
    import math
    return math.ceil(steps)


print(solution(10, 85, 30) == 3)
print(solution(10, 1000000000, 30) == 33333333)