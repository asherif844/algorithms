def validStartingCity(distances, fuel, mpg):
    for i in range(len(distances)):
        dist = distances[i]
        dist+= dist
        
    
    return dist


distances = [5, 25, 15, 10, 15]
fuel = [1, 2, 1, 0, 3]
mpg = 10

validStartingCity(distances, fuel, mpg)
