first = 100

def sum_the_squares(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
        
    return s

def square_the_sums(n):
    s = 0
    for i in range(1,n+1):
        s += i

    return s**2

print str(square_the_sums(first) - sum_the_squares(first))
