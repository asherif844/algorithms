n = 0
while n < 5:
    print( f'Since the value of n is {n} the code will continue')
    n += 1
else:
    print( f'Since the value of n is {n} the code will terminate')


stuff = [5, 10, 15, 20]

new_stuff = [y*y for y in stuff]

newer_stuff = {y: y*y for y in stuff}