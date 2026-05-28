#Przyszło nam powiedzieć, o co chodzi z *args i **kwargs, jak właściwie przekazywać dowolne argumenty oraz jak używać gwiazdki.

import matplotlib.pyplot as plt
import numpy as np

def method_1(*args, **kwargs):
    print("Argumenty pozycyjne (args):", args)
    print("Argumenty nazwane (kwargs):", kwargs)


def method_2(a, b, *args, c=None, **kwargs):
    print("Argument a:", a)
    print("Argument b:", b)
    print("Argument c:", c)
    print("Dodatkowe argumenty pozycyjne (args):", args)
    print("Dodatkowe argumenty nazwane (kwargs):", kwargs)


def main():
    # Przykładowe wywołania funkcji z różnymi argumentami
    method_1(1, 2, 3, 4, x=10, y=20)
    print("\n---\n")
    method_1(a=1, b=2, c=3, d=4, e=5)
    print("\n---\n")
    method_1(1, 2, c=3, d=4)
    print("\n---\n")
    method_1(1, 2, 3, c=4, d=5)
    print("\n---\n")
    method_2(1, 2, 3, 4, c=5, d=6, e=7)

    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plot_with_params(x, y, color='red', linestyle='--', label='sin(x)')

def plot_with_params(x, y, **params):
    plt.plot(x, y, **params)
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()