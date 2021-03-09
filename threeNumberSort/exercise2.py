array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]


def threeNumberSort(array, order):
    # sort array on the left by minimum value of order
    firstValue = order[0]
    lastValue = order[2]
    
    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[idx], array[firstIdx] = array[firstIdx], array[idx]
            firstIdx += 1
    
    LastIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        if array[idx] == lastValue:
            array[idx], array[LastIdx] = array[LastIdx], array[idx]
            LastIdx -=1


    return array




    

    


# def swapNumbers(array, idx):
#     array[idx], array[idx+1] = array[idx+1], array[idx]



threeNumberSort(array, order)