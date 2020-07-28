def insertionSort(array):
    # Write your code here.
    for i in range(len(array)):
        # i = i[1]
        j = i
        while array[j] < array[j-1] and j>0:
            array[j], array[j-1] = array[j-1], array[j]
            j -=1
    return array


        







array = [8, 5, 2, 9, 5, 6, 3]

insertionSort(array)