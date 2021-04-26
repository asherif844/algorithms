def validStartingCity(distances, fuel, mpg):
    bestCityIndex = 0
    startingFuel = 0

    for i in range(len(distances)):
        startingFuel = startingFuel + fuel[i] * mpg
        distanceToTraveltoNextCity = 


    return bestCityIndex


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

validStartingCity(distances, fuel, mpg)
