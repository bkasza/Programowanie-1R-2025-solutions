from argparse import ArgumentParser
from scipy.integrate import solve_ivp
from scipy.constants import g
import numpy as np
import matplotlib.pyplot as plt


def rhs(t, y, length, g) -> list[float]:
    """Prawa strona równania różniczkowedgo dla wahadła

    Args:
        t (float): czas t, konieczny dla solvera ze struktury, tutaj nie uzywamy
        y (float): wektor [theta, omega], gdzie theta to kąt, a omega to prędkość kątowa
        l (float): długość wahadła
        g (float): przyspieszenie ziemskie

    Returns:
        list[float, float]: pochodna wektora [dtheta/dt, domega/dt]
    """
    theta, omega = y  # rozpakowanie dy/dt, dy^2/dt^2
    dtheta_dt = omega  # podhocnda kąta to prędkość kątowa
    domega_dt = -(g / length) * np.sin(
        theta
    )  # zmian prędkości pochodnej to dtheta_dt/dt, wiec tu juz rownanie ruchu
    return [dtheta_dt, domega_dt]  # operujemy na wektorze parametrów


def pendulum_solver(
    tmax:float, length:float, theta0:float, omega0:float, method:str, n_eval:int
) -> tuple[np.ndarray, np.ndarray]:
    """Solver dla równania ruchu wahadła

    Args:
        tmax (float): Maksymalny czas symulacji
        length (float): Długość wahadła
        theta0 (float): Początkowy kąt (w radianach)
        omega0 (float): Początkowa prędkość kątowa [rad/s]
        method (str): Metoda numeryczna do rozwiązania równania różniczkowego
        n_eval (int): Liczba punktów czasowych do ewaluacji

    Returns:
        tuple[np.ndarray, np.ndarray]: Lista z czasem, kątem i prędkością kątową
    """
    t0 = 0
    t_eval = np.linspace(t0, tmax, n_eval)
    sol = solve_ivp(
        rhs,
        [t0, tmax],
        [theta0, omega0],
        args=(length, g),
        t_eval=t_eval,
        method=method,
    )
    return sol.t, sol.y


def plot_phase_diagram(omega, theta):
    plt.figure()
    plt.plot(theta, omega)
    plt.xlabel(r"$\Theta$ [rad]")
    plt.ylabel(r"$\omega$ [rad/s]")
    plt.show()


def plot_time_series(t, theta, omega):
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, theta)
    plt.xlabel("t [s]")
    plt.ylabel(r"$\Theta$ [rad]")
    plt.subplot(2, 1, 2)
    plt.plot(t, omega)
    plt.xlabel("t [s]")
    plt.ylabel(r"$\omega$ [rad/s]")
    plt.tight_layout()
    plt.show()


def main():
    parser = ArgumentParser(description="Program do symulacji wahadła")
    parser.add_argument(
        "-l", "--length", type=float, default=1.0, help="Długość wahadła"
    )
    parser.add_argument(
        "--theta0", type=float, default=2.4, help="Początkowy kąt (w radianach)"
    )
    parser.add_argument(
        "--omega0", type=float, default=1.0, help="Początkowa prędkość kątowa [rad/s]"
    )
    parser.add_argument(
        "--tmax", type=float, default=5.0, help="Czas trwania symulacji [s]"
    )
    parser.add_argument(
        "--method",
        type=str,
        default="RK45",
        choices=["RK45", "RK23", "DOP853", "Radau", "BDF", "LSODA"],
        help="Metoda numeryczna do rozwiązania równania różniczkowego",
    )
    parser.add_argument("--n_eval", type=int, default=1000, help="Liczba punktów czasowych do ewaluacji")
    args = parser.parse_args()
    t, (theta, omega) = pendulum_solver(
        args.tmax, args.length, args.theta0, args.omega0, args.method, args.n_eval
    )

    plot_phase_diagram(omega, theta)

    plot_time_series(t, theta, omega)


if __name__ == "__main__":
    main()
