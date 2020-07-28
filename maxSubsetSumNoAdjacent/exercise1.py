array = [75, 105, 120, 75, 90, 135]

def maxSubsetSumNoAdjacent(array):
    maxSubset = []
    first = array[0]
    second = array[1]
    maxSubset.append(first)
    maxSubset.append(second)
    for i in range(2,len(array)):
        first = array[i-2]
        second = array[i-1] + array[i]
        maxSubset.append(max(first, second))
    return max(maxSubset)





maxSubsetSumNoAdjacent(array)