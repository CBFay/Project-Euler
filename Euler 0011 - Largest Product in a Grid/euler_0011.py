# https://projecteuler.net/problem=11
# created 1.13.2018 by CB Fay

with open("euler_0011.txt", "r") as file:
    lines = file.read()
    nums = lines.split()
    
    def right_product(numbers, index):
        if index % 20 > 15:
            return 0
        product = 1
        for n in numbers[index:index+4]:
            product *= int(n)
        return product

    def down_product(numbers, index):
        if index >= 340:
            return 0    
        product = 1
        for n in range(index, index + 80, + 20):
            product *= int(numbers[n])
        return product

    def downright_product(numbers, index):
        if index % 20 > 15 or index >= 340:
            return 0
        product = 1
        for n in range(index, index + 84, + 21):
            product *= int(numbers[n])
        return product
    
    def downleft_product(numbers, index):
        if index % 20 < 3 or index >= 340:
            return 0
        product = 1
        for n in range(index, index + + 76, + 19):
            product *= int(numbers[n])
        return product
    
    def largest_product():
        functions = [right_product, down_product,
                    downright_product, downleft_product]
        
        maxi = 0
        for i in range(len(nums)):
            for f in range(4):
                this = functions[f](nums, i)
                if this > maxi:
                    maxi = this
        return maxi
            
print(largest_product())
