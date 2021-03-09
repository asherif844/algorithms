array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]


def threeNumberSort(array, order):
    new_array = []

    for j in range(len(order)):
        # print(order[j])
        for i in range(len(array)):
            if order[j]==array[i]:
                new_array.append(array[i])
    return new_array


threeNumberSort(array, order)