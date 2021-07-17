def nextGreaterElement(array):
    lengthOfArray = len(array)
    finalList = []
    for i in range(lengthOfArray):
        # newList = []
        positionInIndex = i
        forwardRange = array[positionInIndex:lengthOfArray]
        backwardRange = array[0: positionInIndex]
        newArray = forwardRange + backwardRange
        originalNumber = newArray[0]
        nge = findNextNumber(newArray,  idx=1)
        # newList.append(nge)

        # print(newArray)
        # print(originalNumber)
        finalList.append(nge)
    return finalList


def findNextNumber(array, idx=1):
    original = array[0]
    while idx < len(array):
        new = array[idx]
        if original < new:
            return new
        else:
            idx += 1
    return -1


    # return originalNumber
array = [2, 5, -3, -4, 6, 7, 2]

nextGreaterElement(array)
