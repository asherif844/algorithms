def sum(a,b):
    return


sum(10,1)



def countdown(n):
    print(n)
    if n <= 0:
        return
    else:
        countdown(n-1)


countdown(5)


def factor(x):
    if x == 1:
        return 1
    else:
        return x*factor(x-1)
    