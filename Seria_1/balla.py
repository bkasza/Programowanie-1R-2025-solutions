from os import name
import numpy as np
import argparse
import sys

def pole_powierzchni(R):
    return 4 * np.pi * R**2

def objetosc_kuli(R):
    return (4/3) * np.pi * R**3

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program oblicza pole powierzchni i objętość kuli o zadanym promieniu R.") #pokazac ze dziala --help
    parser.add_argument('-r', '--radius', type=float, help="Promień kuli", default=1.0)
    args = parser.parse_args()
    R = args.radius
    # args = sys.argv[1:]
    # R = float(args[0]) #druga opcja, ale trzeba pamietac o odpowiednim formacie inputu, tutaj jest to argument, a nie standardowy input
    pole = pole_powierzchni(R)
    print(f"Pole powierzchni kuli o promieniu {R} wynosi: {pole:.2f}")
    objetosc = objetosc_kuli(R)
    print(f"Objętość kuli o promieniu {R} wynosi: {objetosc:.2f}")