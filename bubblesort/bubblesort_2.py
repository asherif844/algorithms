sample = [6, 10, -1, 4, 0, 500, -3350]

isSorted = False

while not isSorted:
    isSorted = True
    counter = 0
    for i in range( len(sample) - 1 - counter):
        if sample[i]> sample[i+1]:
            sample[i], sample[i+1] = sample[i+1], sample[i]
            counter+=1
            isSorted = False

print(sample)
