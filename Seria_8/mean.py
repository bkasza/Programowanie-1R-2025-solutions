from abc import ABC, abstractmethod
from typing import Any

from sys import stdin

class Mean(ABC):
    x = []
    def __init__(self, x: list[float]) -> None:
        if not x:
            raise ValueError("Lista liczb nie może być pusta.")
        self.x = x

    def N(self) -> int:
        """Zwraca liczbę elementów w liście x.

        Returns:
            int: Liczba elementów w liście x.
        """
        return len(self.x)
    
    @abstractmethod
    def __call__(self) -> Any:
        """Wirtualny, bezargumentowy, operator wywołania."""
        pass


class ArithmeticMean(Mean):
    def __call__(self) -> float:
        """Oblicza średnią arytmetyczną elementów w liście x.

        Returns:
            float: Średnia arytmetyczna elementów w liście x.
        """
        return sum(self.x) / self.N()

class GeometricMean(Mean):
    def __call__(self) -> float:
        """Oblicza średnią geometryczną elementów w liście x.

        Returns:
            float: Średnia geometryczna elementów w liście x.
        """
        product = 1.0
        for value in self.x:
            product *= value
        return product ** (1 / self.N())
    
class HarmonicMean(Mean):
    def __call__(self) -> float:
        """Oblicza średnią harmoniczną elementów w liście x.

        Returns:
            float: Średnia harmoniczna elementów w liście x.
        """
        reciprocal_sum = sum(1 / value for value in self.x)
        return self.N() / reciprocal_sum
    

def main():
    print("Podaj liczby oddzielone spacją:")
    input_line = stdin.readline()
    numbers = list(map(float, input_line.split()))

    arithmetic_mean = ArithmeticMean(numbers)
    geometric_mean = GeometricMean(numbers)
    harmonic_mean = HarmonicMean(numbers)

    print(f"Średnia arytmetyczna: {arithmetic_mean():.2f}")
    print(f"Średnia geometryczna: {geometric_mean():.2f}")
    print(f"Średnia harmoniczna: {harmonic_mean():.2f}")

if __name__ == "__main__":
    main()