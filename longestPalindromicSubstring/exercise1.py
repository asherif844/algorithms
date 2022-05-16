
string = 'abaxyzzyxf'


def longestPalindromicSubstring(string):
    longestPalidrome = ''

    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) > len(longestPalidrome) and checkIfLongestPalidrome(substring):
                longestPalidrome = substring

    return longestPalidrome


def checkIfLongestPalidrome(substring):
    leftIdx = 0
    rightIdx = len(substring) - 1
    while leftIdx <= rightIdx:
        if substring[leftIdx] != substring[rightIdx]:
            return False
        else:
            leftIdx += 1
            rightIdx -= 1
    return True


longestPalindromicSubstring(string)
