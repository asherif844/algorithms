sample_array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]


def sort_array(array):
    lengthOfArray = len(array)
    currentIndex = 0
    while currentIndex < lengthOfArray - 1:
        smallestIndex = currentIndex
        for i in range(currentIndex+1, lengthOfArray):
            if array[smallestIndex] > array[i]:
                smallestIndex = i
        swap(array, currentIndex, smallestIndex)
        currentIndex+=1
    return final3(array)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def final3(array):
    return array[-3:]

sort_array(sample_array)
