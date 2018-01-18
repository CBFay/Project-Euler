# https://projecteuler.net/problem=12
# created 1.18.2018 by CB Fay

def triangles(limit):
    tri = 1
    i = 2
    while divisors(tri) < limit:
        tri += i
        i += 1
    print(tri)
            
            
def divisors(number):
    divs = 0
    i = 1
    squareroot = int(number ** .5) + 1
    while i < squareroot:
        if number % i == 0:
            divs += 2
        i += 1
    return divs
            
triangles(500)
