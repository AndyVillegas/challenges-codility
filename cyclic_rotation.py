# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    copy_A = A.copy()
    for index in range(0, len(A)):
        new_index = index + K
        if new_index >= len(A):
            new_index = new_index % len(A)
        A[new_index] = copy_A[index]
    return A

print(solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8])
print(solution([1, 2, 3, 4], 4) == [1, 2, 3, 4])