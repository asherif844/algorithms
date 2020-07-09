# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.


def productSum(array, multiplier=1):
    sum_ = 0
    for i in array:
        if type(i) is list:
            sum_ += productSum(i, multiplier + 1)
        else:
            sum_ += i

    return sum_ 


array_new = [1, [1, 2], 2, 3, 4, 5]


productSum(array_new)
