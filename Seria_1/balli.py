import numpy as np
import sys

#tu jest najwazniejsze zeby stosowac sie do odpowiednich rodzajow inputow, jeden standardowy, drugi jako argument
def pole_powierzchni(R):
    return 4 * np.pi * R**2

def objetosc_kuli(R):
    return (4/3) * np.pi * R**3


if __name__ == "__main__":

    print("Program oblicza pole powierzchni i objętość kuli o zadanym promieniu R.")
    # R = float(input("Podaj1 promień kuli: "))
    # pole = pole_powierzchni(R)
    # print(f"Pole powierzchni kuli o promieniu {R} wynosi: {pole:.2f}")
    for line in sys.stdin:
        if 'q' == line.strip():
            break
        else:
            R = float(line.strip())
            pole = pole_powierzchni(R)
            print(f"Pole powierzchni kuli o promieniu {R} wynosi: {pole:.2f}")
            objetosc = objetosc_kuli(R)
            print(f"Objętość kuli o promieniu {R} wynosi: {objetosc:.2f}")
