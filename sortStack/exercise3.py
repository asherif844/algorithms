def sortStack(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()

    sortStack(stack)

    insertIntoStack(stack, top)
    return stack


def insertIntoStack(stack, value):
    if len(stack) == 0 or value >= (stack[len(stack) - 1]):
        stack.append(value)
        return
    top = stack.pop()

    insertIntoStack(stack, value)
    stack.append(top)


stack = [-5, 2, -2, 4, 3, 1]

sortStack(stack)
