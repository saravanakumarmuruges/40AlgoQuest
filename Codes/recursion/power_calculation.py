'''
Write a recursive function to calculate 𝑥𝑛
(x raised to the power n). The function should take two integers, x and n, as input and return 𝑥𝑛
Input: x = 2, n = 5
Output: 32
'''

x=2
n=5

def power(x,n):
    if n==1:
        return x
    return x*power(x,n-1)

print(power(x,n))
