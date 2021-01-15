array = [2, 1, 5, 2, 3, 3, 4]
array = [2, 1, 5, 3, 3, 2, 4]
array = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]

def firstDuplicateValue(array):
    lowestRepeatedIndex = len(array)
    
    for i in range(len(array)):
        primaryNumber = array[i]
        for j in range(i+1, len(array)):
            secondaryNumber = array[j]
            if secondaryNumber == primaryNumber:
                lowestRepeatedIndex = min(lowestRepeatedIndex, j)

                # lowestRepeatedIndex.append(secondaryNumber)
    if lowestRepeatedIndex == len(array):
        return -1

    return array[lowestRepeatedIndex]

firstDuplicateValue(array)
