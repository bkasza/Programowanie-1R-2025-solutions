
import re
from factorial import iterative, recursive
import matplotlib.pyplot as plt
import sys

def plot(time_data, values, title, filename):
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].plot(range(1, len(time_data) + 1), time_data, label="Czas obliczeń", color="blue")
    ax[0].set_title(f"Czas obliczeń {title}")
    ax[0].set_xlabel("n")
    ax[0].set_ylabel("Czas (s)")
    ax[0].legend()
    ax[1].plot(range(1, len(values) + 1), values, label="Wartości silni", color="red")
    ax[1].set_title(f"Wartości silni {title}")
    ax[1].set_xlabel("n")
    ax[1].set_ylabel("Wartość silni")
    ax[1].legend()
    ax[1].set_yscale("log")
    fig.tight_layout()
    fig.savefig(filename, dpi=300)

def main(N):
    iterative_times = []
    iterative_values = []
    recursive_times = []
    recursive_values = []  
    for n in range(1, N + 1):
        iterative_value, iterative_time = iterative(n)
        recursive_value, recursive_time = recursive(n)
        iterative_times.append(iterative_time)
        recursive_times.append(recursive_time)
        iterative_values.append(iterative_value)
        recursive_values.append(recursive_value)
    plot(iterative_times, iterative_values*0, "Iteracyjna", r"plots/iterative_factorial.png")
    plot(recursive_times, recursive_values*0, "Rekurencyjna", r"plots/recursive_factorial.png")


if __name__ == "__main__":
    args = sys.argv[1:]
    N = int(args[0])
    main(N)
    print('wykonano')