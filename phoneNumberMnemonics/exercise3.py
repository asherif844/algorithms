phoneNumber = "3524947428"


def phoneNumberMnemonics(phoneNumber):
    allNumbers = []
    aNumber = [0] * len(phoneNumber)

    phoneNumberMnemonicsHelper(0, phoneNumber, aNumber, allNumbers)

    return allNumbers


def phoneNumberMnemonicsHelper(idx, phoneNumber, aNumber, allNumbers):
    if len(phoneNumber) == idx:
    
        allNumbers.append(''.join(aNumber))
    
    else:
        digit = phoneNumber[idx]
        letters = digit_letters[digit]
        for letter in letters:
            aNumber[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, aNumber, allNumbers)    



digit_letters = {
    "0": ['0'],
    "1": ['1'],
    "2": ['a', 'b', 'c'],
    "3": ['d', 'e', 'f'],
    "4": ['g', 'h', 'i'],
    "5": ['j', 'k', 'l'],
    "6": ['m', 'n', 'o'],
    "7": ['p', 'q', 'r', 's'],
    "8": ['t', 'u', 'v'],
    "9": ['w', 'x', 'y', 'z']}


phoneNumberMnemonics(phoneNumber)
