a = 1
b = 1
c = 0
fsum = 0

while (b <= 4000000):
    if (b % 2 == 0):
        #print "b: " + str(b)
        fsum += b
    c = a + b
    a = b
    b = c

print "The sum is " + str(fsum)

    


