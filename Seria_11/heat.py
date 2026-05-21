from argparse import ArgumentParser
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def solve_heat(T0: float, T1: float, T2: float, T3: float, T4: float):
    alpha = 2.0
    dx = 1.0
    dt = (dx**2) / (4.0 * alpha)
    L = 50
    N = int(L / dx)
    
    T = np.full((N, N), T0)
    
    T[0, :] = T1   # górna krawędź
    T[:, -1] = T2  # prawa krawędź
    T[-1, :] = T3  # dolna krawędź
    T[:, 0] = T4   # lewa krawędź
    
    fig, ax = plt.subplots(figsize=(7, 6))
    cax = ax.imshow(T, cmap='hot', vmin=0, vmax=100, origin='upper', interpolation='nearest') 
    fig.colorbar(cax, label='Temperatura [$^\circ$C]')
    ax.set_title("Rozkład temperatury w płytce")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    
    def update(frame):
        for _ in range(10):
            T_new = 0.25 * (T[2:, 1:-1] + T[:-2, 1:-1] + T[1:-1, 2:] + T[1:-1, :-2])
            
            T[1:-1, 1:-1] = T_new
            
        cax.set_array(T)
        
        current_time = frame * 10 * dt
        ax.set_title(f"T(x, y) (t = {current_time:.2f} s)")
        
        return cax,

    anim = FuncAnimation(fig, update, frames=200, interval=30, blit=False)
    plt.show()

def main():
    parser = ArgumentParser(description="Model przewodnictwa cieplnego płytki metalowej (Równanie ciepła)")
    parser.add_argument("T0", type=float, help="Początkowa temperatura wnętrza płytki")
    parser.add_argument("T1", type=float, help="Temperatura na górnej krawędzi")
    parser.add_argument("T2", type=float, help="Temperatura na prawej krawędzi")
    parser.add_argument("T3", type=float, help="Temperatura na dolnej krawędzi")
    parser.add_argument("T4", type=float, help="Temperatura na lewej krawędzi")
    
    args = parser.parse_args()
    
    solve_heat(args.T0, args.T1, args.T2, args.T3, args.T4)

if __name__ == "__main__":
    main()


