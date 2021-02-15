def nonConstructibleChange(coins):
    coins.sort()
    currentChangeCreated = 0
    allChangeCreated = []
    for coin in coins:
          
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated = currentChangeCreated + coin
       

        
    return currentChangeCreated + 1
    # return currentChangeCreated + 1
    # return allChangeCreated,coins

coins = [5, 7, 1, 1, 2, 3, 22]
nonConstructibleChange(coins)
