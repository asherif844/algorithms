def bubbleSort(array):
    isSorted = False
    counter = 0
    while isSorted is False:
        isSorted = True
        for i in range(len(array) - 1):
            leftIdx = array[i]
            rightIdx = array[i+1]
            if leftIdx > rightIdx:
                swapped(i, i+1, array)
                isSorted = False

    return array


def swapped(left, right, array):
    array[left], array[right] = array[right], array[left]


sample = [8, 5, 2, 9, 5, 6, 3]
bubbleSort(sample)
