def productsum(arrays, multiplier=1):
    sum_ = 0
    for element in arrays:
        if type(element) is list:
            sum_ += productsum(element, multiplier + 1)
        else:
            sum_ += element
    return sum_ * multiplier

array_new = [1,[1,2],2,3,4,5]


productsum(array_new)