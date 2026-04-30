from abc import ABC, abstractmethod
from argparse import ArgumentParser
from math import pi
from typing import override, Self
import numpy as np

"""Przykład dziedziczenia na starym zadaniu z circles. By dodać sobie sprawdzanie typu w metodzie intersection, musimy użyć typu Self, który jest dostępny od Pythona 3.11.
Jest to specjalny typ, który odnosi się do klasy, w której jest używany. Dzięki temu możemy wskazać, że metoda intersection przyjmuje jako argument obiekt tej samej klasy, co klasa, w której jest zdefiniowana.
"""

class Figure(ABC):
    """Generujemy klasę abstrakcyjną, która będzie bazą dla różnych figur geometrycznych."""
    @abstractmethod
    def circumference(self) -> float:
        """Returns the circumference of the figure."""
        pass

class Circle(Figure):
    def __init__(self, x0: float, y0: float, r: float):
        self.x0 = x0
        self.y0 = y0
        self.r = r

    @override
    def circumference(self) -> float:
        return 2 * pi * self.r

    def intersection(self, second_circle: Self) -> int:
        centre_pos_1 = np.array([self.x0, self.y0])
        centre_pos_2 = np.array([second_circle.x0, second_circle.y0])
        distance = np.linalg.norm(centre_pos_1 - centre_pos_2)
        
        if distance > self.r + second_circle.r:
            return 0
        elif distance == self.r + second_circle.r:
            return 1
        else:
            return 2

def main():
    parser = ArgumentParser()
    parser.add_argument("--x0", type=float, default=0, help="X coordinate of the first circle center")
    parser.add_argument("--y0", type=float, default=0, help="Y coordinate of the first circle center")
    parser.add_argument("--r", type=float, default=1, help="Radius of the first circle")
    parser.add_argument("--x1", type=float, default=1, help="X coordinate of the second circle center")
    parser.add_argument("--y1", type=float, default=0, help="Y coordinate of the second circle center")
    parser.add_argument("--r1", type=float, default=1, help="Radius of the second circle")
    args = parser.parse_args()
    c1 = Circle(args.x0, args.y0, args.r)
    c2 = Circle(args.x1, args.y1, args.r1)
    print("Obwód pierwszego okręgu", c1.circumference())
    print("Obwód drugiego okręgu", c2.circumference())
    print("Liczba punktów przecięcia okręgów", c1.intersection(c2))

if __name__ == "__main__":
    main()

