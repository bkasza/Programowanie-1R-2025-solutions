from argparse import ArgumentParser
from CyRK import nbsolve_ivp, nb_diffeq_addr, nbsolve2_ivp, pysolve_ivp
from numba import njit
import matplotlib.pyplot as plt
import numpy as np
import time

def rhs_py(t:float, vec:np.ndarray, a:float, b:float, c:float, d:float) -> np.ndarray:
    """Prawa strona równania - czysty Python"""
    x, y = vec[0], vec[1]
    dx_dt = (a - b * y) * x
    dy_dt = (-c + d * x) * y
    return np.array([dx_dt, dy_dt], dtype=np.float64)

@njit
def rhs(t:float, vec:np.ndarray, a:float, b:float, c:float, d:float) -> np.ndarray:
    """Prawa strona równania różniczkowego dla modelu Lotki-Volterry

    Args:
        t (float): czas t, konieczny dla solvera ze struktury, tutaj nie uzywamy
        y (np.ndarray): wektor [x, y], gdzie x to liczba ofiar, a y to liczba drapieżników
        a (float): współczynnik wzrostu ofiar
        b (float): współczynnik śmiertelności ofiar z powodu drapieżników
        c (float): współczynnik śmiertelności drapieżników
        d (float): współczynnik wzrostu drapieżników z powodu ofiar

    Returns:
        np.ndarray: pochodna wektora [dx/dt, dy/dt]
    """
    x, y = vec[0], vec[1]
    dx_dt = (a - b * y) * x
    dy_dt = (-c + d * x) * y
    return np.array([dx_dt, dy_dt])

@njit
def rhs_cfunc(dy: np.ndarray, t: float, vec: np.ndarray, args: np.ndarray):
    """Prawa strona rownania solvera nbsolve2_ivp o innej sygnaturze funkcji."""
    x = vec[0]
    y = vec[1]
    
    a = args[0]
    b = args[1]
    c = args[2]
    d = args[3]
    
    dy[0] = (a - b * y) * x
    dy[1] = (-c + d * x) * y

def lotka_volterra_solver(tmax:float, n_eval:int, x0:float, y0:float, *args) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Solver dla równania ruchu modelu Lotki-Volterry przy uzyciu CyRK's nbsolve_ivp

    Args:
        tmax (float): Maksymalny czas symulacji
        x0 (float): Początkowa liczba ofiar
        y0 (float): Początkowa liczba drapieżników
        args (tuple[float]): Krotka z parametrami (a, b, c, d)

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Czas, liczba ofiar, liczba drapieżników
    """
    t0 = 0.0
    t_eval = np.linspace(t0, tmax, n_eval)
    sol = nbsolve_ivp(rhs, (t0, tmax), np.array([x0, y0], dtype=np.float64), args=args, t_eval=t_eval, warnings=False)
    return sol.t, sol.y[0], sol.y[1]


def lotka_volterra_solver2(tmax:float, n_eval:int, x0:float, y0:float, *args) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Solver dla równania ruchu modelu Lotki-Volterry przy uzyciu CyRK's nbsolve2_ivp

    Args:
        tmax (float): Maksymalny czas symulacji
        x0 (float): Początkowa liczba ofiar
        y0 (float): Początkowa liczba drapieżników
        args (tuple[float]): Krotka z parametrami (a, b, c, d)

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Czas, liczba ofiar, liczba drapieżników
    """
    t0 = 0.0
    t_eval = np.linspace(t0, tmax, n_eval)
    
    diffeq_address = nb_diffeq_addr(rhs_cfunc)
    
    args_arr = np.array(args, dtype=np.float64)
    sol = nbsolve2_ivp(diffeq_address, (t0, tmax), np.array([x0, y0], dtype=np.float64), args=args_arr, t_eval=t_eval)
    return sol.t, sol.y[0], sol.y[1]


def lotka_volterra_solver_pysolve(tmax:float, n_eval:int, x0:float, y0:float, *args) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Solver dla równania ruchu modelu Lotki-Volterry przy uzyciu CyRK's pysolve_ivp"""
    t0 = 0.0
    t_eval = np.linspace(t0, tmax, n_eval)
    sol = pysolve_ivp(rhs_py, (t0, tmax), np.array([x0, y0], dtype=np.float64), args=args, t_eval=t_eval)
    return sol.t, sol.y[0], sol.y[1]


def plot_population_dynamics(t, x, y):
    plt.figure()
    plt.plot(t, x, label='Liczba ofiar')
    plt.plot(t, y, label='Liczba drapieżników')
    plt.xlabel('t')
    plt.legend()
    plt.show()

def main():
    parser = ArgumentParser(description="Solver dla modelu Lotki-Volterry (CyRK)")
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
    
    # rozgrzewka jitow, czyli kompilacja funkcji i bibliotek
    _ = lotka_volterra_solver(args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d)
    _ = lotka_volterra_solver2(args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d)
    
    t0_time = time.perf_counter()
    lotka_volterra_solver(args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d)
    t1_time = time.perf_counter()
    print(f"nbsolve_ivp (Numba 1) czas: {t1_time - t0_time:.5f} sekund")
    
    t2_time = time.perf_counter()
    lotka_volterra_solver2(args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d)
    t3_time = time.perf_counter()
    print(f"nbsolve2_ivp (Numba 2/C++) czas: {t3_time - t2_time:.5f} sekund")
    
    t4_time = time.perf_counter()
    t, x, y = lotka_volterra_solver_pysolve(args.tmax, args.n_eval, args.x0, args.y0, args.a, args.b, args.c, args.d)
    t5_time = time.perf_counter()
    print(f"pysolve_ivp (Cython/Python) czas: {t5_time - t4_time:.5f} sekund")
    
    plot_population_dynamics(t, x, y)

if __name__ == "__main__":
    main()
