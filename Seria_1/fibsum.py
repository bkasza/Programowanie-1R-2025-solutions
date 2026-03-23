import timeit


def fibsum(limit=3000000):
    "Fibonacci iteracyjnie z kontrola sumy"
    a, b = 0, 1
    sum = 0  # F(0) = 0, so we start with 0
    index = 1
    while b < limit:
        if index % 2 == 0:  
            sum += b
        a, b = b, a + b
        index += 1
    print(f"Suma elementów o wskaznikach podzielnych przez 2 wynosi {sum}")


def fibsum_fast(limit=3000000):
    total_sum = 0
    # F(2) = 1, F(4) = 3
    f_prev = 1
    f_curr = 3
    total_sum = f_prev + f_curr 
    while True:
        f_next = 3 * f_curr - f_prev
        if f_next >= limit:
            break
        total_sum += f_next
        f_prev, f_curr = f_curr, f_next
    print(total_sum)

if __name__ == "__main__":
    timeit_time = timeit.timeit("fibsum()", globals=globals(), number=1)
    print(f"fibsum() took {timeit_time:.6f} seconds")
    timeit_time_fast = timeit.timeit("fibsum_fast()", globals=globals(), number=1)
    print(f"fibsum_fast() took {timeit_time_fast:.6f} seconds")
