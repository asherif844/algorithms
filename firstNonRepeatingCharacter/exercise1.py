def firstNonRepeatingCharacter(string):
    try:
        wordCount = obtainDictionary(string)
        word = list(wordCount.keys())[list(wordCount.values()).index(0)]
        index = list(string).index(word)
        return index
    except:
        return -1


def obtainDictionary(string):
    wordCount = {}
    count = 0
    for idx in range(len(string)):
        if string[idx] not in wordCount:
            wordCount[string[idx]] = 0
        else:
            wordCount[string[idx]] += 1
    return wordCount


def getFirstLetter(wordCount):
    return list(x for x in wordCount.keys() if x == '0')

string = 'faadabcbbebdfc'
firstNonRepeatingCharacter(string)
