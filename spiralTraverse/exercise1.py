def spiralTraverse(array):
    result = []
    SR, ER = 0, len(array) - 1
    SC, EC = 0, len(array[0]) - 1

    while SR <= ER and SC <= EC:
        for col in range(SC, EC+1):
            result.append(array[SR][col])
        for row in range(SR+1, ER+1):
            result.append(array[row][EC])
        for col in reversed(range(SC, EC)):
            if SR == ER:
                break
            result.append(array[ER][col])
        for row in reversed(range(SR+1, ER)):
            if SC==EC:
                break
            result.append(array[row][SC])
        SR +=1
        SC +=1
        ER -=1
        EC -=1

    return result




array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

# [1, 2, 3, 4]
# [12, 13, 14, 5]
# [11, 16, 15, 6]
# [10, 9, 8, 7]
spiralTraverse(array)