
height = 4
maxSteps = 2


def staircaseTraversal(height, maxSteps):
    return NumOfWaysToTop(height, maxSteps)


def NumOfWaysToTop(height, maxSteps):
    if height <=1:
        return 1
    
    NumOfWays = 0
    for step in range(1, min(height, maxSteps)+1):
        NumOfWays = NumOfWays + NumOfWaysToTop(height - step, maxSteps)

staircaseTraversal(height, maxSteps)