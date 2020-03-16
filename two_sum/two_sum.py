numbers = [3, 5, -4, 8, 12, 1, -1, 6]
targetSum = 11


def twoNumberSum(numbers, targetSum):
    combinations = []
    for j in range(len(numbers)):
        number = numbers[j]
        if targetSum - number in numbers:
            combinations.append([number, targetSum-number])
    return combinations


