def solution(N):
    binary = bin(N)[2::]
    gaps = get_binary_gaps(binary)
    if(len(gaps) == 0):
        return 0
    return len(max(gaps))

def get_binary_gaps(binary):
    is_open = False
    current_binary = ''
    gaps = []
    for binary_part in binary:
        if(binary_part == '1'):
            if(len(current_binary) > 0):
                gaps.append(current_binary)
                current_binary = ''
            is_open = not is_open
        else:
            current_binary = current_binary + binary_part
    return gaps

assert(solution(1041) == 5)
assert(solution(32) == 0)
assert(solution(15) == 0)