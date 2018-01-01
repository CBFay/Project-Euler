# https://projecteuler.net/problem=4
# created 1.1.2018 by CB Fay

def ispalindrome(n):
    num = str(n)
    i = 0
    j = len(num)-1
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True
        
def largest_3digit_palindrome():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if i * j > largest and ispalindrome(i * j):
                largest = i * j
    return largest

print(largest_3digit_palindrome())
