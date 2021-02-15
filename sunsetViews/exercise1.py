def sunsetViews(buildings, direction):
    max_height = 0
    sunset = []
    if direction =='WEST':
        for i in range(0, len(buildings)):
            if buildings[i] > max_height:
                max_height = buildings[i]
                sunset.append(max_height)
    if direction == 'EAST':
        for i in reversed(range(0, len(buildings))):
            if buildings[i] > max_height:
                max_height = buildings[i]
                sunset.append(i)

    # Write your code here.
    return sorted(sunset)


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = "WEST"

sunsetViews(buildings, direction)
