# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 1 and A[0] == 1:
        return 2
    ordered_A = sorted(A)
    if len(ordered_A) == 0 or (len(ordered_A) >= 1 and ordered_A[0] != 1):
        return 1
    if ordered_A[0] == 1 and ordered_A[-1] == len(ordered_A):
        return ordered_A[-1] + 1
    number_found = -1
    while number_found == -1 and len(ordered_A)//2 != 0:
        middle_index = len(ordered_A)//2
        if (middle_index + 1) < len(ordered_A) and ordered_A[middle_index] + 1 != ordered_A[middle_index + 1]:
            number_found = ordered_A[middle_index] + 1
        if middle_index > 0 and  ordered_A[middle_index] - 1 != ordered_A[middle_index - 1]:
            number_found = ordered_A[middle_index] - 1
        left = ordered_A[:middle_index]
        right = ordered_A[middle_index:]
        first_number_left = left[0]
        possible_last_number_left = first_number_left + len(left) - 1
        if possible_last_number_left == left[-1]:
            ordered_A = right
        else:
            ordered_A = left
    return number_found

print(solution([2]) == 1)
print(solution([2, 3, 1, 5]) == 4)