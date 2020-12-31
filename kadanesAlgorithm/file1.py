def kadanesAlgorithm(array):
    fullArray = []
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
        if maxEndingHere == num:
            fullArray.append(maxEndingHere)
    return maxSoFar, fullArray


array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
kadanesAlgorithm(array)
