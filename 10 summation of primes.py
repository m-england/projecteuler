def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def sum_all_primes(n):
    sump = 0
    for i in range(2, n+1):
        if isPrime(i):
            sump+=i
    
    return sump

answer = sum_all_primes(2000000)
print str(answer)

