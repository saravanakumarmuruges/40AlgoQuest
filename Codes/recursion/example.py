# Factorial of numbers

n=5

def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(n))