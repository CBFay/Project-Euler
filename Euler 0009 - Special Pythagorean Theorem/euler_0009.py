# https://projecteuler.net/problem=9
# created 1.11.2018 by CB Fay

from math import sqrt

def solution(target):
    for a in range(1, target//2):
        for b in range(a, target//2):
            c = sqrt(a**2 + b**2)
            if a**2 + b**2 == c**2 and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)
                exit()

solution(1000)
