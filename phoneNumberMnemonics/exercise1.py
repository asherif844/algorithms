phoneNumber = "1905"
def phoneNumberMnemonics(phoneNumber):
    
    mnemonic = []
    mnemonic_list = []
    for i in range(len(phoneNumber)):
        
        if int(phoneNumber[i]) < 2:
            mnemonic.append(phoneNumber[i])
        
        if int(phoneNumber[i]) >= 2:
            digit = findNumber(phoneNumber[i])[0]
            for j in range(len(digit)):
                mnemonic.append(digit[j])

    return ''.join(mnemonic)

def findNumber(i):
    letters = {
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']}
    
    
    
    return letters[str(i)]

phoneNumberMnemonics(phoneNumber)

