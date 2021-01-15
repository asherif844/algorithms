array = [2, 1, 5, 2, 3, 3, 4]
array = [2, 1, 5, 3, 3, 2, 4]
array = [9, 13, 6, 2, 3, 5, 5, 5, 3, 2, 2, 2, 2, 4, 3]


def firstDuplicateValue(array):
    seen = set()
    for value in array:

        if value in seen:
            return value
        seen.add(value)
    return -1


firstDuplicateValue(array)
