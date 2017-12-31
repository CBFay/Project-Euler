# https://en.wikipedia.org/wiki/Triangular_number
# https://projecteuler.net/problem=1
# created 12.31.2017 by CB Fay
  
def L(a, b):
    """Solve using triangular number formula"""
    return a * ((b-1)//a) * (((b-1)//a) + 1) // 2
    
print(L(3, 1000) + L(5, 1000) - L(15, 1000))
