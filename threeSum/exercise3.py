import random
random_list = random.sample(range(0,10), 5)


A = random_list[0]
B = random_list[1]
C = random_list[2]
D = random_list[3] 
E = random_list[4]

ABCD = int(str(A)+str(B)+str(C)+str(D))
E = int(str(E))
DCBA = int(str(D)+str(C)+str(B)+str(A))

PRODUCT = ABCD * E

while DCBA != PRODUCT:
    random_list = random.sample(range(0,10), 5)
    A = random_list[0]
    B = random_list[1]
    C = random_list[2]
    D = random_list[3] 
    E = random_list[4]
    ABCD = int(str(A)+str(B)+str(C)+str(D))
    E = int(str(E))
    DBCA = int(str(D)+str(C)+str(B)+str(A))
    PRODUCT = ABCD * E
    if DCBA == PRODUCT:
        break
print('ABCD:',ABCD)
print('E:', E)
print('DCBA:', DCBA)