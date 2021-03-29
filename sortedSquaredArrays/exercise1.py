def sortedSquaredArray(array):
    squaredArray = []
    idx = 0
    for i in range(len(array)):
        newValue = array[i]**2
        squaredArray.append(newValue)
        # if

    # Write your code here.
    return sorted(squaredArray)


array = [-10, -5, 0, 5, 10]


sortedSquaredArray(array)
