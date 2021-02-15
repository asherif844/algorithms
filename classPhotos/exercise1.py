import json


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights = sorted(redShirtHeights)
    blueShirtHeights = sorted(blueShirtHeights)

    if max(redShirtHeights) == max(blueShirtHeights):
        return False

    backRow = redShirtHeights if max(redShirtHeights) > max(blueShirtHeights) else blueShirtHeights
    frontRow = redShirtHeights if max(redShirtHeights) < max(blueShirtHeights) else blueShirtHeights

    for i in range(len(redShirtHeights)):
        backStudent = backRow[i]
        frontStudent = frontRow[i]
        if backStudent <= frontStudent:
            return False

    return True



    # return redShirtHeights, blueShirtHeights, max(redShirtHeights), max(blueShirtHeights)


# with open('data.json', 'r') as f:
#     data = json.load(f)


# redShirtHeights = data['redShirtHeights']
# blueShirtHeights = data['blueShirtHeights']

redShirtHeights = [19, 2, 4, 6, 2, 3, 1, 1, 4]
blueShirtHeights = [21, 5, 4, 4, 4, 4, 4, 4, 4]

classPhotos(redShirtHeights, blueShirtHeights)
