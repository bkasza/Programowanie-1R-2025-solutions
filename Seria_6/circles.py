from argparse import ArgumentParser
from typing import Self
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as CirclePatch
from math import pi


class Inf:
    """Klasa reprezentująca nieskończoną liczbę ułożeń/punktów (np. dla w pełni pokrywających się okręgów)."""
    
    def __str__(self) -> str:
        return "inf"
    
    def __repr__(self) -> str:
        return "inf"


class Circle:
    def __init__(self, x0: float, y0: float, r: float):
        """
        Inicjalizacja klasy Circle, która reprezentuje okrąg na płaszczyźnie. Przyjmuje współrzędne środka (x0, y0) oraz promień r.
        Inicjalizacja jest metodą specjalną (__init__), która jest wywoływana automatycznie podczas tworzenia obiektu klasy Circle. Umożliwia ustawienie początkowych wartości atrybutów obiektu.

        Args:
            x0 (float): odcięta środka okręgu
            y0 (float): rzędna środka okręgu
            r (float): promień okręgu
        """
        self.x0 = x0
        self.y0 = y0
        self.r = r
        # Self to specjalny typ, który odnosi się do instancji klasy, w której jest używany. Umożliwia odwoływanie się do atrybutów i metod tej instancji wewnątrz klasy.

    def circumference(self) -> float:
        """Nasza pierwsza metoda klasy. Oblicza obwód okręgu oraz zwraca jego wartość.

        Returns:
            float: obwód okręgu
        """
        return 2 * pi * self.r

    def intersection(self, second_circle: "Circle") -> int | Inf:
        """Metoda intersection oblicza liczbę punktów przecięcia dwóch okręgów. Przyjmuje jako argument drugi okrąg (second_circle) i zwraca liczbę punktów przecięcia (0, 1 lub 2).

        Args:
            second_circle ("Circle"): drugi okrąg, z którym porównujemy pierwszy okrąg (self).
                
                Typowanie argumentów wewnątrz klasy, w której są definiowane, bywa problematyczne. Ponieważ klasa nie została jeszcze w pełni zainicjowana, użycie jej samej nazwy wywołałoby NameError. Zamiast tego z reguły stosuje się jedno z obejść:
                1. "Circle" (typ jako string) - technika odroczonego sprawdzania typu (forward reference). Powszechne i spójne (szczególnie w adnotacjach metod statycznych).
                2. Typ 'Self' (z modułu typing) - mechanizm stosowany od Pythona 3.11 precyzyjniej modelujący obiekty przy użyciu dziedziczenia. 

        Returns:
            int | Inf: Liczba punktów przecięcia dwóch okręgów (0, 1, 2 lub jako nieskończoność zwracamy obiekt klasy Inf)
        """
        # Spoiler biblioteki numpy. Oczywiście można po prostu policzyć z pitagorasa (odległość euklidesowa).
        centre_pos_1 = np.array([self.x0, self.y0])
        centre_pos_2 = np.array([second_circle.x0, second_circle.y0])
        distance = np.linalg.norm(centre_pos_1 - centre_pos_2)

        # Używamy np.isclose do precyzyjnych porównań floatów
        if np.isclose(distance, 0.0) and np.isclose(self.r, second_circle.r):
            return Inf()  # pełne pokrycie

        # Albo są za daleko od siebie lub jeden jest całkowicie wewnątrz durgiego bez styczności
        elif (
            distance > self.r + second_circle.r
            and not np.isclose(distance, self.r + second_circle.r)
        ) or (
            distance < abs(self.r - second_circle.r)
            and not np.isclose(distance, abs(self.r - second_circle.r))
        ):
            return 0

        # Okręgi styczne (mają dokładnie 1 punkt styku)
        # styczność zewnętrzna (suma promieni) lub wewnętrzna (różnica promieni)
        elif np.isclose(distance, self.r + second_circle.r) or np.isclose(
            distance, abs(self.r - second_circle.r)
        ):
            return 1

        # We wszystkich pozostałych przypadkach okręgi przecinają się na 2 punktach
        else:
            return 2

    def __call__(self) -> None:
        """Drugą bardzo ważną metodą specjalną jest metoda __call__. By ją wywołać musimy zawołać stworzoną instancję klasy."""
        self.plot_circle()

    def plot_circle(self) -> None:
        """Metoda plot_circle służy do rysowania figury okręgu na płaszczyźnie, korzystając z matplotlib.

        Returns:
            None: Metoda nie zwraca żadnej wartości, a jedynie wyświetla wykres z narysowanym okręgiem.
        """
        plt.figure(figsize=(6, 6))
        circle = CirclePatch((self.x0, self.y0), self.r, fill=False)
        plt.gca().add_patch(circle)
        plt.xlim(self.x0 - self.r - 1, self.x0 + self.r + 1)
        plt.ylim(self.y0 - self.r - 1, self.y0 + self.r + 1)
        plt.show()

    @staticmethod
    def plot_two_circles(c1: "Circle", c2: "Circle") -> None:
        """Metoda statyczna plot_two_circles służy do rysowania dwóch okręgów na tej samej płaszczyźnie, korzystając z matplotlib.
        Jest oznaczona jako statyczna, ponieważ nie odwołuje się do żadnych atrybutów instancji klasy (self) i może być wywoływana bez potrzeby tworzenia obiektu klasy Circle.

        Args:
            c1 (Circle): pierwszy okrąg do narysowania
            c2 (Circle): drugi okrąg do narysowania
        Returns:
            None: Metoda nie zwraca żadnej wartości, a jedynie wyświetla wykres z narysowanymi okręgami.
        """
        plt.figure(figsize=(6, 6))
        circle1 = CirclePatch(
            (c1.x0, c1.y0), c1.r, fill=False, edgecolor="blue", label="Circle 1"
        )
        circle2 = CirclePatch(
            (c2.x0, c2.y0), c2.r, fill=False, edgecolor="red", label="Circle 2"
        )
        plt.gca().add_patch(circle1)
        plt.gca().add_patch(circle2)
        plt.xlim(
            min(c1.x0 - c1.r, c2.x0 - c2.r) - 1, max(c1.x0 + c1.r, c2.x0 + c2.r) + 1
        )
        plt.ylim(
            min(c1.y0 - c1.r, c2.y0 - c2.r) - 1, max(c1.y0 + c1.r, c2.y0 + c2.r) + 1
        )
        plt.legend()
        plt.show()


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--x0", type=float, default=0, help="Odcięta środka pierwszego okręgu"
    )
    parser.add_argument(
        "--y0", type=float, default=0, help="Rzędna środka pierwszego okręgu"
    )
    parser.add_argument("--r0", type=float, default=3, help="Promień pierwszego okręgu")
    parser.add_argument(
        "--x1", type=float, default=1, help="Odcięta środka drugiego okręgu"
    )
    parser.add_argument(
        "--y1", type=float, default=0, help="Rzędna środka drugiego okręgu"
    )
    parser.add_argument("--r1", type=float, default=4, help="Promień drugiego okręgu")
    args = parser.parse_args()
    c1 = Circle(args.x0, args.y0, args.r0)
    c2 = Circle(args.x1, args.y1, args.r1)
    print("Obwód pierwszego okręgu", c1.circumference())
    print("Obwód drugiego okręgu", c2.circumference())
    print("Liczba punktów przecięcia okręgów", c1.intersection(c2))
    # c1() # wywołanie metody __call__ dla pierwszego okręgu, co spowoduje narysowanie tego okręgu na płaszczyźnie
    # c2()
    Circle.plot_two_circles(
        c1, c2
    )  # wywołanie metody statycznej do narysowania obu okręgów na tej samej płaszczyźnie


if __name__ == "__main__":
    main()
