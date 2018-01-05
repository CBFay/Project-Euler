# https://projecteuler.net/problem=7
# created 01.05.2018 by CB Fay

def isprime(n):
    for i in range(2, int(n ** (1/2)+1)):
        if n  % i == 0:
            return False
    return True

def nthprime(n):
    primes = 0
    i = 1
    while primes < n:
        i += 1
        if isprime(i):
            primes += 1
    return i

print(nthprime(10001))
