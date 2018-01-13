# https://projecteuler.net/problem=10
# created 1.12.2018 by CB Fay

def primesum(n):
    composites = set()
    p_sum = 0
    for p in range(2, n):
        if p in composites:
            continue
        p_sum += p
        for multiple in range(p, (n // p)+1):
            composites.add(multiple*p)
    print(p_sum)
                
primesum(2000000)
