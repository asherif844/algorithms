

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            swap(i, j, array)
        i += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

moveElementToEnd(array, toMove)
