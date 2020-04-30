def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)


def getNewLetter(letter, newKey):
    newLetterCode = ord(letter) + newKey
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode%122)