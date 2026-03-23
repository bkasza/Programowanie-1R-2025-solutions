from factorial_utils import ifactorial, rfactorial
from timeit import default_timer as timer
import sys

def iterative(n):
    t1 = timer()
    result_i = ifactorial(n)
    t2 = timer()
    return result_i, t2 - t1

def recursive(n):
    t3 = timer()
    result_r = rfactorial(n)
    t4 = timer()
    return result_r, t4 - t3

if __name__ == "__main__":
    args = sys.argv[1:]
    n = int(args[0])
    iterative_value, iterative_time = iterative(n)
    print(f"Silnia {n} wynosi {iterative_value}, obliczenie iteracyjne zajęło {(iterative_time)*1e3:.5f} ms")
    recursive_value, recursive_time = recursive(n)
    print(f"Silnia {n} wynosi {recursive_value}, obliczenie rekurencyjne zajęło {(recursive_time)*1e3:.5f} ms")