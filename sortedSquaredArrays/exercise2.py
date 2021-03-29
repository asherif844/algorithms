array = [-10, -5, 0, 5, 10]


def sortedSquaredArray(array):
    new_array = []
    rightPointer = len(array) - 1
    leftPointer = 0
    while leftPointer <= rightPointer:
        if abs(array[rightPointer])>abs(array[leftPointer]):
            new_array.append(array[rightPointer]**2)
            rightPointer-=1
        else:
            #  abs(array[rightPointer])<abs(array[leftPointer]):
            new_array.append(array[leftPointer]**2)
            leftPointer+=1
    new_array = new_array[::-1]
    return new_array



sortedSquaredArray(array)
