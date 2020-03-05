numbers = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


def twoNumberSum(numbers, targetSum):
    num = {}
    for j in numbers:
        if targetSum - j in numbers and j != (targetSum - j):
            return [targetSum-j, j]
        else:
            num[j] = True
    return []


twoNumberSum(numbers, targetSum)
