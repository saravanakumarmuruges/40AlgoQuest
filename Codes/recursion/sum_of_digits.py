'''Problem Statement: 
Write a recursive function that takes a positive integer n as input and returns the sum of its digits.
Input: 1234
Output: 10
'''


a = 12345
def sumofdigits(n):
    if n<10:
        return n
    return (n%10) + sumofdigits(n//10)

print(sumofdigits(a))