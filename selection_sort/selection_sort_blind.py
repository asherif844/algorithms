def sorted_sort(array):
    original_index = 0
    while original_index < len(array) - 1:
        smallest_index = original_index
        for i in range(smallest_index+1, len(array)):
            if array[i] < array[smallest_index]:
                smallest_index = i
        swap(smallest_index, original_index, array)
        original_index += 1
    return array


def swap(smallest_index, original_index, array):
    array[smallest_index], array[original_index] = array[original_index], array[smallest_index]
    # return array

old_array = [5, 4, 3, 2, -5, -6, 10, 200, 36, 0]


print(sorted_sort(old_array))
