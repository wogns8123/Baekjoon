def factorial(n):
    if n ==0:
        return 1
    elif n<2:
        return n
    else:
        return n*factorial(n-1)

n = int(input())
print(factorial(n))