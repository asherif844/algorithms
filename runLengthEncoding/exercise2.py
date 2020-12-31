string = "AAAAAAAAAAAAABBCCCCDD"

def runLengthEncoding(string_):
    characters = []
    currentRunLength = 1
    for i in range(1,len(string_)):
        currentCharacter = string_[i]
        previousCharacter = string_[i-1]
        if currentCharacter != previousCharacter:
            characters.append(str(currentRunLength))
            characters.append(previousCharacter)
            currentRunLength = 0
        currentRunLength +=1
    characters.append(str(currentRunLength))
    characters.append(previousCharacter)
    return "".join(characters)


runLengthEncoding(string)