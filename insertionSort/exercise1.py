sample = [6, 10, -1, 4, 0, 500, -3350]

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j]<array[j-1] and j>0:
            swap(j, j-1, array)
            j-= 1
    return array

def swap(a,b,array):
    array[a], array[b] = array[b], array[a]




insertionSort(sample)