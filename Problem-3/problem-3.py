# find fast factorization algo 
# current is just trial division
def prime_factors(n):
    primes = []
    f = 3
    # remove factors of 2
    while n % 2 == 0:
        primes.append(2)
        n = n//2
    # init for odd factors
    if n == 1:
        return primes
    else:
        f = 3
    # end if prime
    while(True):
        if n < f*f:
            primes.append(n)
            return primes
        else:
            # trial division
            q = n//f
            r = n % f
            # loop on odd ints
            if r > 0:
                f += 2
            else:
                primes.append(f)
                n = q
print(max(prime_factors(600851475143))) #6857
