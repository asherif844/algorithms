def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    total_speed = 0
    if fastest == True:
        redShirtSpeeds = sorted(redShirtSpeeds)
        blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=True)
        for i in range(len(redShirtSpeeds)):
            redSpeed = redShirtSpeeds[i]
            bluespeed = blueShirtSpeeds[i]
            speed = max(redSpeed, bluespeed)
            total_speed += speed
    elif fastest == False:
        redShirtSpeeds = sorted(redShirtSpeeds)
        blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=False)
        for i in range(len(redShirtSpeeds)):
            redSpeed = redShirtSpeeds[i]
            bluespeed = blueShirtSpeeds[i]
            speed = max(redSpeed, bluespeed)
            total_speed += speed
    return total_speed


redShirtSpeeds = [5, 5, 3, 9, 2]
blueShirtSpeeds = [3, 6, 7, 2, 1]
fastest = True

tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest)
