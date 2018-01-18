# https://projecteuler.net/problem=13
# created 1.18.2018 by CB Fay

with open("euler_0013.txt") as file:
    numbers = file.read().split('\n')
    result = 0
    for n in numbers:
        result += int(n)
    print(str(result)[:10])
