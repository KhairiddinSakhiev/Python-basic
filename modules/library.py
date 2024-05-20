def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact


def is_polindrom(n):
    if n==n[::-1]:
        return True
    else:
        return False

