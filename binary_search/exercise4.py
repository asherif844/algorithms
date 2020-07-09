def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) // 2
    potentialMatch = array[middle]
    if potentialMatch == target:
        return middle
    if potentialMatch < target:
        return binarySearchHelper(array, target, middle+1, right)
    if potentialMatch > target:
        return binarySearchHelper(array, target, left, middle - 1)


array = [1, 0, 21, 33, 45, 45, 61, 71, 72, 73]
array = sorted(array)
target = 33

binarySearch(array, target)
