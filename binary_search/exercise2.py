# time O(log N)
# space 0(1)
sample_array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]


def binarySearch(array, target):

    return helper(array, target, 0, len(array)-1)


def helper(array, target, left, right):
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            return helper(array, target, left, middle-1)
        elif target > potentialMatch:
            return helper(array, target, middle+1, right)
    return -1


binarySearch(sample_array, 55)
