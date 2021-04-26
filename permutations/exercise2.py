def getPermutations(array):
    if not len(array):
        return []
    if len(array) == 1:
        return array
    else:
        permutation = getPermutations(array[1:])
        character = array[0]
        permutations = []

        for perm in permutation:
            for i in range(len(perm)+1):
                permutations.append(perm[:i]+character+perm[i:])
    return permutations



array = 'abcd'

getPermutations(array)