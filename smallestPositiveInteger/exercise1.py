A = [1, 3, 6, 4, 1, 2]
# A = [1,2,3]
# A = [-1, -3]

def solution(A):
    A = sorted(A)
    if max(A)<0:
        return 1
    for i in range(1, len(A)):
        array1 = A[i-1]
        array2 = A[i]
        if array2 - array1 >1:
            return array2 - 1
        else:
            continue
    return max(A)+1




solution(A)