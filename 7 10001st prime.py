which_prime =10001
curr_prime = 0
i = 2

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


while curr_prime < which_prime:
    if isPrime(i):
        curr_prime += 1
        
    i += 1
        
print i-1
                    
