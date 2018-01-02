# https://projecteuler.net/problem=6
# created 1.1.2018 by CB Fay

sumsquares = 0
for i in range(1, 101):
    sumsquares += i**2

squaresums = 0
for i in range(1, 101):
    squaresums += i
squaresums **= 2

print(squaresums - sumsquares)
