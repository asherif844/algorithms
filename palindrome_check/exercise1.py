sample_string = 'abcdcbaa'

def isPalindrome(string):
    reverseString = ''
    lengthOfString = len(string)
    for i in reversed(range(lengthOfString)):
        reverseString+=string[i]
    return string == reverseString

isPalindrome(sample_string)