from math import factorial

def sum_a(x, n):
    'exp(x)'
    sum = 0
    for k in range(0, n+1):
        sum += x**k/factorial(k)

    return sum

def sum_b(x, n):
    'cos(x)'
    sum = 0
    for k in range(0, n+1):
        sum += (-1)**k * x**(2*k)/factorial(2*k)

    return sum