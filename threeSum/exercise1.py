def threeNumberSum(array, targetSum):
    candidate = []
    array = sorted(array)
    for i in range(len(array)-2):
        print(i)
        left_index = i+1
        right_index = len(array) - 1
        while left_index < right_index:
            sum_of_all = array[i]+array[left_index]+array[right_index]
            if sum_of_all == targetSum:
                candidate.append([array[i], array[left_index], array[right_index]])
                left_index+=1
                right_index-=1
            if sum_of_all < targetSum:
                left_index+=1
            if sum_of_all > targetSum:
                right_index-=1
    return candidate

    return array




array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))