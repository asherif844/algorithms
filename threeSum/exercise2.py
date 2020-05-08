import random

letters = ['L', 'E', 'M', 'L', 'F', 'T','A', 'B','G','D']
ALFA = str(letters.index('A'))+str(letters.index('L'))+str(letters.index('F'))+str(letters.index('A'))
BETA = str(letters.index('B'))+str(letters.index('E'))+str(letters.index('T'))+str(letters.index('A'))
GAMA = str(letters.index('G'))+str(letters.index('A'))+str(letters.index('M'))+str(letters.index('A'))
DELTA = str(letters.index('D'))+str(letters.index('E'))+str(letters.index('L'))+str(letters.index('T'))+str(letters.index('A'))
SUM_OF_ALL = int(ALFA) + int(BETA) + int(GAMA)    

while SUM_OF_ALL != int(DELTA):
    random.shuffle(letters)
    ALFA = str(letters.index('A'))+str(letters.index('L'))+str(letters.index('F'))+str(letters.index('A'))
    BETA = str(letters.index('B'))+str(letters.index('E'))+str(letters.index('T'))+str(letters.index('A'))
    GAMA = str(letters.index('G'))+str(letters.index('A'))+str(letters.index('M'))+str(letters.index('A'))
    DELTA = str(letters.index('D'))+str(letters.index('E'))+str(letters.index('L'))+str(letters.index('T'))+str(letters.index('A'))
    SUM_OF_ALL = int(ALFA) + int(BETA) + int(GAMA)
    if SUM_OF_ALL == int(DELTA):
        break

print('ALFA: ', ALFA)
print('BETA: ', BETA)
print('GAMA: ', GAMA)
print('DELTA: ', DELTA)
