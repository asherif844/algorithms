sample_string = 'abccbad'


def isPalindrome(string):
    rightIdx = len(string) - 1
    leftIdx = 0
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx+=1
        rightIdx-=1
    return True

isPalidrome(sample_string)