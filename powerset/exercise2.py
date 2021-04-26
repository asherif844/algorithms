# this is the iterative approach
def powerset(array):
    fullArray = [[]]
    for element in array:
        for i in range(len(fullArray)):
            currentSubset = fullArray[i]
            fullArray.append(currentSubset + [element])
    return fullArray

        
    

array = [1, 2, 3]
powerset(array)
