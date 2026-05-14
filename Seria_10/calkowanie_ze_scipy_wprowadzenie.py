#%%

# a co to był problem cauchy? 

"wezmy rownanie macierzowe dx/dt = A x, gdzie A jest macierzą n x n, a x jest wektorem n. Rozwiązujemy ze względu na x(t) znająć x0"
#%%

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def f(t, x):
    """A = [[0, 1]], [-1, 0]], czyli odpowiada rownaniu
    dx/dt = v
    dv/dt = -x
    czyli w jednej linijce jest to: d^2x/dt^2 = -x
    """
    A = np.array([[0, 1], [-1, 0]])
    
    
    return A @ x

def solver(t_eval, x0):
    sol = solve_ivp(f, (0, t_eval[-1]), x0, t_eval=t_eval)
    return sol.t, sol.y[0], sol.y[1]

t_max = 10
t_eval = np.linspace(0, t_max, 100)
x0 = np.array([1, 0])
t, x, y = solver(t_eval, x0)



# %%
plt.plot(t, x, label='x(t)')
# %%
"""
(function) def solve_ivp(
    fun: Unknown,
    t_span: Unknown,
    y0: Unknown,
    method: str = 'RK45',
    t_eval: Unknown | None = None,
    dense_output: bool = False,
    events: Unknown | None = None,
    vectorized: bool = False,
    args: Unknown | None = None,
    **options: Unknown
) -> Unknown
"""