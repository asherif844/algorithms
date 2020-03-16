def selectionSort(array):
    current_index = 0
    while current_index < len(array) - 1:
        smallest_index = current_index
        for i in range(current_index+1, len(array)):
            if array[smallest_index]>array[i]:
                smallest_index = i
        swap(current_index, smallest_index, array)
        current_index += 1
    return array    

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



array = [5, 1, 3, 15, -2, 45, 8]

selectionSort(array)