array =  [3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2]

def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0

    while numElementsVisited < len(array):
        if numElementsVisited  > 0 and currentIdx ==0: 
            return False 
        numElementsVisited += 1
        currentIdx = getNextIdx(currentIdx, array)
    return currentIdx ==0


def getNextIdx(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if currentIdx >= 0 else nextIdx + len(array)


hasSingleCycle(array)