# https://projecteuler.net/problem=3
# created 1.1.2018 by CB Fay

def isprime(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True                   

def biggestprimefactor(n):
    for i in range(2, n//2):
        if n % i == 0 and isprime(n/i):
            return n//i
    return

print(biggestprimefactor(600851475143))
