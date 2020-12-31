string_ = 'AAAAAAAAAAAAABBCCCCDZ'

def runLengthEncoding(string_):
    # Write your code here.
    encodedstringCharacters = []
    currentRunLength = 1
    for i in range(1, len(string_)):
        currentC = string_[i]
        previousC = string_[i-1]
        if currentC != previousC or currentRunLength == 9:
            encodedstringCharacters.append(str(currentRunLength))
            encodedstringCharacters.append(previousC)
            currentRunLength = 0
        
        currentRunLength += 1
    
    encodedstringCharacters.append(str(currentRunLength))
    encodedstringCharacters.append(string_[len(string_)-1])

    return ''.join(encodedstringCharacters)


# if __name__ == '__main__':
#     runLengthEncoding(string_)

runLengthEncoding(string_)