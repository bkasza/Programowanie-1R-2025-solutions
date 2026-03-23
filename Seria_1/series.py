import argparse
from sums import sum_a, sum_b

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", type=float, help="Wartość x")
    parser.add_argument("-n", type=int, help="Wartość n")
    args = parser.parse_args()
    sum_a = sum_a(args.x, args.n)
    sum_b = sum_b(args.x, args.n)
    print(f"sum_a(x, n) = {sum_a:.4f}")
    print(f"sum_b(x, n) = {sum_b:.4f}")
