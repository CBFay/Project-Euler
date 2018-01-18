# https://projecteuler.net/problem=14
# created 1.18.2018 by CB Fay

def collatz_chain(number):
    n = number
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        length += 1
    return length


def big_chain():
    maxi = 0, 0
    for i in range(1, 1000000):
        size = collatz_chain(i)
        if size > maxi[1]:
            maxi = i, size
    return maxi
            
print(big_chain())
