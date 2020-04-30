sample_string = 'abcdcbaa'

def isPalindrome(string):
    """this is a sample doc string that has no intrinsic value"""
    reverseString = ''
    lengthOfString = len(string)
    for i in reversed(range(lengthOfString)):
        reverseString+=string[i]
    return string == reverseString
    """this is a sample doc string that has no intrinsic value2"""

print(isPalindrome.__doc__)