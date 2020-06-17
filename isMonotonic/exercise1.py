def isMonotonic(array):
    direction = []
    if len(array) <= 2:
        return True
    for i in range(len(array)-1):
        left_index = array[i]
        right_index = array[i+1]
        if right_index == left_index:
            direction.append('equal')
        if right_index > left_index:
            direction.append('increasing')
        if right_index < left_index:
            direction.append('decreasing')
    if set(direction) == {'decreasing', 'increasing'}:
        return False
    if len(set(direction)) == 3:
        return False
    else:
        return True

isMonotonic([1, 2, 0])

