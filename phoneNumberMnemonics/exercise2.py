phoneNumber = "3524947428"


def phoneNumberMnemonics(phoneNumber):
    all_combos = []
    combo = ["0"] * len(phoneNumber)

    phoneNumberMnemonicsHelper(0, phoneNumber, combo, all_combos)

    return all_combos


def phoneNumberMnemonicsHelper(idx, phoneNumber, combo, all_combos):
    if idx == len(phoneNumber):
        mnemonic = ''.join(combo)
        all_combos.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = digit_letters[digit]
        for letter in letters:
            combo[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, combo, all_combos)


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
