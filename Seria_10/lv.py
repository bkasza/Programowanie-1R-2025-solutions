from argparse import ArgumentParser
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def rhs(
    t: float, vec: list[float], a: float, b: float, c: float, d: float
) -> list[float]:
    """Prawa strona równania różniczkowego dla modelu Lotki-Volterry

    Args:
        t (float): czas t, konieczny dla solvera ze struktury, tutaj nie uzywamy
        y (float): wektor [x, y], gdzie x to liczba ofiar, a y to liczba drapieżników
        a (float): współczynnik wzrostu ofiar
        b (float): współczynnik śmiertelności ofiar z powodu drapieżników
        c (float): współczynnik śmiertelności drapieżników
        d (float): współczynnik wzrostu drapieżników z powodu ofiar

    Returns:
        list[float, float]: pochodna wektora [dx/dt, dy/dt]
    """
    x, y = vec  # rozpakowanie wektora (ofiary, drapieżniki)
    dx_dt = (a - b * y) * x
    dy_dt = (-c + d * x) * y
    return [dx_dt, dy_dt]


def lotka_volterra_solver(
    tmax: float, n_eval: int, x0: float, y0: float, *args
) -> tuple[list[float], list[float], list[float]]:
    """Solver dla równania ruchu modelu Lotki-Volterry

    Args:
        tmax (float): Maksymalny czas symulacji
        x0 (float): Początkowa liczba ofiar
        y0 (float): Początkowa liczba drapieżników
        args (tuple[float]): Krotka z parametrami (a, b, c, d)

    Returns:
        tuple[list[float], list[float], list[float]]: Lista z czasem, liczbą ofiar i liczbą drapieżników
    """
    t0 = 0
    t_eval = np.linspace(t0, tmax, n_eval)
    sol = solve_ivp(rhs, [t0, tmax], [x0, y0], args=args, t_eval=t_eval)
    return sol.t, sol.y[0], sol.y[1]


def plot_population_dynamics(t, x, y):
    plt.figure()
    plt.plot(t, x, label="Liczba ofiar")
    plt.plot(t, y, label="Liczba drapieżników")
    plt.xlabel("t")
    plt.legend()
    plt.show()


def main():
    parser = ArgumentParser(description="Solver dla modelu Lotki-Volterry")
    parser.add_argument("-a", type=float, default=0.5)
    parser.add_argument("-b", type=float, default=0.02)
    parser.add_argument("-c", type=float, default=0.4)
    parser.add_argument("-d", type=float, default=0.01)
    parser.add_argument("--x0", type=float, default=50)
    parser.add_argument("--y0", type=float, default=3)
    parser.add_argument("--tmax", type=float, default=140.0)
    parser.add_argument(
        "--n_eval", type=int, default=1000, help="Liczba punktów czasowych do ewaluacji"
    )

    args = parser.parse_args()
    t, x, y = lotka_volterra_solver(
        args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d
    )
    plot_population_dynamics(t, x, y)


if __name__ == "__main__":
    main()
