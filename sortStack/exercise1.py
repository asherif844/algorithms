def sortStack(stack):
    if len(stack) == 0:
        return stack
    top = stack.pop()

    sortStack(stack)

    insertToStack(stack, top)
    return stack


def insertToStack(stack, value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insertToStack(stack, value)
    stack.append(top)


stack = [-5, 2, -2, 4, 3, 1]

sortStack(stack)
