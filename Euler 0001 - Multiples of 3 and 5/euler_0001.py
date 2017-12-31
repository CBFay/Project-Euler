# https://projecteuler.net/problem=1
# created 12.30.2017 by CB Fay

def answer():
    multiples = set()
    for i in range(3,1000,3):
        multiples.add(i) 
    for i in range(5,1000,5):
        multiples.add(i)
    print(sum(multiples))


answer()
