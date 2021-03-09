def searchInSortedMatrix(matrix, target):
    for i in range(len(matrix)):
        row = matrix[i]
        for j in row:
            if j == target:
                return [i, row.index(j)]
    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

target = 44


searchInSortedMatrix(matrix, target)
