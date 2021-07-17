def recursive_add(number1):
    if number1 <= 1:
        return number1
    
    return int(number1) + int(recursive_add(number1 - 1))


number1 = 5

recursive_add(number1)
