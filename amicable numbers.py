import math

def d(n):
    total = 0
    for i in n:
        total += i
    return total

def find_divisors(n):
    divisors = []
    for i in range(1, n-1):
        if (n % i == 0):
            divisors.append(i)
    return divisors

def find_amicables(x,y):
    

amicables = []
allsums = [0]

for i in range(1,10):
    total = d(find_divisors(i))
    print find_amicables(total)
    
    allsums.append(total)

    print find_amicables(total) 


print "List of amicables: ",
print amicables
#print d(amicables)
