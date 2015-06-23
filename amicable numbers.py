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
    if (y > len(allsums)):
        return
    if (allsums[y] == x and y != x):
        amicables.append(x)
        amicables.append(y)

amicables = []
allsums = [0]

for i in range(1,10000):
    total = d(find_divisors(i))
    allsums.append(total)
    find_amicables(i, total)

print "List of amicables: ",
print amicables
print d(amicables)
