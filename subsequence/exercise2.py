array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


seqIdx = 0
arrIdx = 0
while seqIdx < len(sequence) and arrIdx < len(array):
    if array[arrIdx]==sequence[seqIdx]:
        seqIdx+=1
    arrIdx+=1

print(seqIdx, len(sequence))