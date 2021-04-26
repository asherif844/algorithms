def validStartingCity(distances, fuel, mpg):
    cityIdx = len(distances) - 1
    finalCityIdx = reorderPair(distances, fuel, mpg, cityIdx)

    return finalCityIdx


def reorderPair(distances, fuel, mpg, cityIdx):
    fuelAvailable = 0
    distanceToTravel = 0
    cities = len(distances)
    for i in range(cities):
        if cityIdx == cities - 1:
            return cityIdx
        fuelAvailable += fuel[i] * mpg
        distanceToTravel += distances[i]
        if distanceToTravel > fuelAvailable:
            removedDistance = distances.pop(0)
            removedFuel = fuel.pop(0)
            distances.append(removedDistance)
            fuel.append(removedFuel)
            cityIdx += 1
            reorderPair(distances, fuel, mpg, cityIdx)
    
    return cityIdx


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

validStartingCity(distances, fuel, mpg)
