import sys
import matplotlib.pyplot as plt
from math import pi


def arctan(x, K):
    result = 0
    for n in range(0, K + 1):
        result += (-1) ** n * (x ** (2 * n + 1)) / (2 * n + 1)
    return result


def pi_from_Machine(K):
    pi_Machine = 4 * (4 * arctan(1 / 5, K) - arctan(1 / 239, K))
    return pi_Machine


def main(N):
    pi_approx_values = []
    for K in range(1, N + 1):
        pi_approx = pi_from_Machine(K)
        pi_approx_values.append(pi_approx)
    plt.plot(range(1, N + 1), pi_approx_values, label="Przybliżenie liczby π")
    plt.axhline(y=pi, color="r", linestyle="--", label="Liczba π")
    plt.title(f"Oszacowanie π dla K = {N} wyniosło: {pi_approx:.6f}")
    plt.savefig(r"plots\pi_approximation.png", dpi=300)


if __name__ == "__main__":
    args = sys.argv[1:]
    N = int(args[0])
    main(N)
