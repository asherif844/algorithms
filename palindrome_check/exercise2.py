# space complexity = O(N)
# time complexity = O(N^2)

sample_string = 'abcdcba'


def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i+1)


isPalindrome(sample_string)