def sumOfNumber(value):
    if value ==0:
        return value
    else:
        return value + sumOfNumber(value - 1)



sumOfNumber(5)