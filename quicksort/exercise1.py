from turtle import right


array = [8, 5, 2, 9, 5, 6, 3]


def quickSort(array):
    quickSorthelper(array, 0, len(array) - 1)
    return array


def quickSorthelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return

    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while leftIdx <= rightIdx:
        if array[leftIdx]>array[pivotIdx] and array[rightIdx]<array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx]<=array[pivotIdx]:
            leftIdx +=1
        if array[rightIdx]>=array[pivotIdx]:
            rightIdx -=1

    swap(pivotIdx, rightIdx, array)



def swap(l, r, array):
    array[l], array[r] = array[r], array[l]


quickSort(array)