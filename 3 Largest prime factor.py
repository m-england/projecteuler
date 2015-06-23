def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n /= i
        i = i + 1
    print factors
    return max(factors)


print prime_factors(600851475143)
