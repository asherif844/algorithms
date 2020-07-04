def longestPeak(array):
    # Write your code here.
    longestLenghtPeak = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i-2 
        while leftIdx >=0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -=1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx +=1
        currentPeakLenght = rightIdx - leftIdx - 1
        longestLenghtPeak = max(longestLenghtPeak, currentPeakLenght)
        i = rightIdx
    return longestLenghtPeak


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]


longestPeak(array)
