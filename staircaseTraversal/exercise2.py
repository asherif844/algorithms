height = 4
maxSteps = 2


def staircaseTraversal(height, maxSteps):
    return NumberOfWaysToTop(height, maxSteps)


def NumberOfWaysToTop(height, maxSteps):
    if height <= 1:
        return 1
    numberOfWays = 0
    for i in range(1, min(height, maxSteps)+1):
        numberOfWays += NumberOfWaysToTop(height - i, maxSteps)

    return numberOfWays


staircaseTraversal(height, maxSteps)
