
final = []
def smallestDifference(arrayOne, arrayTwo):
    arrayOne = sorted(arrayOne)
    arrayTwo = sorted(arrayTwo)
    differences = []
    for i in range(len(arrayOne)):
        first = arrayOne[i]

        for j in range(len(arrayTwo)):
            second = arrayTwo[j]
            difference = abs(first - second)
            differences.append([first, second, difference])

    return lowest(differences)

def lowest(differences):
    differences.sort(key=lambda x:x[2])
    return differences[0][:2]


arrayOne =  [10, 0, 20, 25, 2200]
arrayTwo = [1005, 1006, 1014, 1032, 1031]

smallestDifference(arrayOne, arrayTwo)