def balancedBrackets(string):

    opening = ['[', '(', '{']
    closing = [']', ')', '}']
    matching = {']': '[', ')': '(', '}': '{'}

    allChars = []

    for char in string:
        if char in opening:
            allChars.append(char)
        elif char in closing:
                if len(allChars) == 0:
                    return False
                if allChars[-1] == matching[char]:
                        allChars.pop()
                else:
                    return False

    return True if len(allChars) == 0 else False
string = "([])(){}(())()()"


balancedBrackets(string)

