
array = [1, 2, 3, 4, 5, 6, 7, 0, 9]


def arrayOfProducts(array):
    new_array = [0] * len(array)
    if 0 in array:
    
        for i in range(len(array)):
            if array[i] == 0:
                new_array[i] = findProduct(array)

    # else:
    #     new_array[i] = findProduct(array) / array[i]
    else:
        for i in range(len(array)):
            new_array[i] = findProduct(array)/array[i]
    return new_array


def findProduct(array):
    # drop 0 from the array
    if 0 in array:
        array.remove(0)
        array.append(1)
    productSum = 1
    for i in array:
            productSum = productSum * i

    return productSum


arrayOfProducts(array)
# findProduct(array)
