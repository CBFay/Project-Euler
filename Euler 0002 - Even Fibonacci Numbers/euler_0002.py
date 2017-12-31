# https://projecteuler.net/problem=2
# created 12.30.2017 by CB Fay

s = 0 # sum
a = 1
b = 2

while b < 4000000:
    if b % 2 == 0:
        s += b
        
    a, b = b, a+b    

print(s)
