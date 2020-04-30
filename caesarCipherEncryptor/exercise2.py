# A = [1, 3, 6, 4, 1, 2]
# A = [1,2,3]
# A = [-1, -3]

def solution(A):
    B = sorted(A)
    for i in range(len(A)-1):
        current_number = B[i]
        next_number = B[i+1]
        if next_number - current_number > 1 and current_number >0:
            return current_number + 1
    return max(B)+1 if next_number - current_number == 1 else 1


assert solution([1, 3, 6, 4, 1, 2])==5
assert solution([1,2,3])==4
assert solution([-1, -3])==1