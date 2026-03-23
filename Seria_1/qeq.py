from math import sqrt

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta == 0:
        x = -b / (2*a)
        return f"Równanie ma jedno rozwiązanie: x = {x:.2f}"
    elif delta < 0:
        x1 = (-b + 1j*sqrt(abs(delta))) / (2*a)
        x2 = (-b - 1j*sqrt(abs(delta))) / (2*a)
        return f"Równanie ma dwa rozwiązania zespolone: x1 = {x1:.2f}, x2 = {x2:.2f}"
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        return f"Równanie ma dwa rozwiązania rzeczywiste: x1 = {x1:.2f}, x2 = {x2:.2f}"

if __name__ == "__main__":
    a = float(input("Podaj a: "))
    b = float(input("Podaj b: "))
    c = float(input("Podaj c: "))

    assert a != 0, "To nie jest równanie kwadratowe, a musi być różne od 0."
    result = solve_quadratic(a, b, c)
    print(result)
