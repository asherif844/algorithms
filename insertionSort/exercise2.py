def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j] < array[j-1] and j>0:
            swap(j, j-1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


array = [8, 5, 2, 9, 5, 6, 3]
insertionSort(array)