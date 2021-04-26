# this is the recursive approach
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]

    element = array[idx]
    subset = powerset(array, idx - 1)

    for i in range(len(subset)):
        currentSubset = subset[i]
        subset.append(currentSubset + [element])
    return subset


array = [1, 2, 3]
powerset(array)
