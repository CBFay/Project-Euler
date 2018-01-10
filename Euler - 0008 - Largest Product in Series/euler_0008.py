# https://projecteuler.net/problem=8
# created 1.10.2018 by CB Fay

with open("euler_0008.txt", "r") as file:
    number = file.read().replace('\n', '')

def longest_product(n, length):
        start = 0
        end = length
        maxi = [0, '']
        while end < len(n): 
            sub = n[start:end]
            product = 1
            for i in sub:
                product *= int(i)
                if product > maxi[0]:
                    maxi[0] = product
                    maxi[1] = sub
            start += 1
            end += 1
        return maxi
            
print(longest_product(number, 13))
