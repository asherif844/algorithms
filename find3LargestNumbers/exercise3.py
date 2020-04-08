sample_array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]



def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    # compare current number to the 3rd value in the array
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2) #TODO
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1) #TODO
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0) #TODO


def shiftAndUpdate(array,num,idx):
    for i in range(idx + 1):
        if i == idx: 
            array[i] = num
        else:
            array[i] = array[i + 1]

findThreeLargestNumbers(sample_array)