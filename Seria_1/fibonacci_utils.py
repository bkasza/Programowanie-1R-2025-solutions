def fibi(n):
    "Fibonacci iteracyjnie"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def frbi(n):
    "Fibonacci rekurencyjnie"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return frbi(n - 1) + frbi(n - 2)
    
    