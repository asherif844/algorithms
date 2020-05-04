sample_string = 'abcdcbaa'
def isPalindrome(word):
    # return word == word[::-1]
    return word == "".join(reversed(word))


isPalindrome(sample_string)

"".join(reversed(sample_string))