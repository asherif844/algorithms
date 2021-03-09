

string = 'Everything is Awesome!'


def reverseWordsInString(string):
    word = []
    startOfWord = 0
    for i in range(len(string)):
        character = string[i]
        if character == ' ':
            word.append(string[startOfWord:i])
            startOfWord = i
        elif string[startOfWord] == ' ':
            word.append(' ')
            startOfWord = i
    word.append(string[startOfWord:])

    return reversal_of_word(word)


def reversal_of_word(word):
    reversedWord = []
    spots = len(word) - 1
    while spots >= 0:
        reversedWord.append(word[spots])
        spots = spots - 1
    return ''.join(reversedWord)


reverseWordsInString(string)
