goal = 1000

for a in range(1,goal):
    for b in range(a+1,goal):
        c = goal - a - b
        if ((a**2 + b**2 == c**2) and (a+b+c==goal)):
            print a,b,c,
            print a * b * c
                
