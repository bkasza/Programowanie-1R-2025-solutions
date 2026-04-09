import sys

# Wersja już bardziej koneserska, demonstrująca przeciążanie operatorów (+ oraz |).


class Resistor:
    def __init__(self, resistance: float = 0):
        """Inicjalizacja klasy Resistor, która reprezentuje rezystor elektryczny. Przyjmuje opcjonalny argument resistance, który określa wartość rezystancji. Domyślnie jest ustawiona na 0.

        Args:
            resistance (float, optional): Wartość oporu opornika. Defaults to 0.
        """

        # W ten sposób definiujemy atrybut prywatny, który jest dostępny tylko wewnątrz klasy.
        self.__R = resistance

    def get_resistance(self) -> float:
        """Oblicza i zwraca wartość rezystancji opornika. Jest to metoda publiczna, która umożliwia dostęp do prywatnego atrybutu __R.

        Returns:
            float: Wartość rezystancji opornika.
        """
        return self.__R

    def set_resistance(self, resistance: float) -> None:
        """Ustawia wartość rezystancji opornika. Jest to metoda publiczna, która umożliwia modyfikację prywatnego atrybutu __R.

        Args:
            resistance (float): Nowa wartość rezystancji opornika.
        """
        self.__R = resistance

    def __add__(self, other: "Resistor") -> "Resistor":
        """Przeciążenie operatora dodawania (+).
        Implementuje naturalne połączenie szeregowe rezystorów.

        Args:
            other (Resistor): Drugi rezystor w gałęzi

        Returns:
            Resistor: Rezystor o rezystancji zastępczej
        """
        # Możemy tu pobrać opór bezpośrednio z atrybutu prywatnego (self.__R oraz other.__R),
        # ponieważ metoda jest zdefiniowana wewnątrz tej samej klasy.
        return Resistor(self.__R + other.__R)

    def __or__(self, other: "Resistor") -> "Resistor":
        """Przeciążenie operatora bitowego OR (|).
        Używamy pythonowy znak OR jako symbolu połączenia równoległego (||).

        Args:
            other (Resistor): Drugi rezystor

        Raises:
            ValueError: Jeśli którykolwiek z rezystorów ma rezystancję równą zero.

        Returns:
            Resistor: Rezystor o rezystancji zastępczej
        """
        if self.__R == 0 or other.__R == 0:
            raise ValueError(
                "Rezystancja nie może być równa zero w połączeniu równoległym."
            )
        return Resistor(1 / (1 / self.__R + 1 / other.__R))


def main() -> None:
    """Wczytujemy ze standardowego wejścia dwie wartości oporu rezystorów. Zwracamy wartość oporu zastępczego dla połączenia równoległego i szeregowego."""
    r0 = float(sys.stdin.readline())
    r1 = float(sys.stdin.readline())
    res1 = Resistor(r0)
    res2 = Resistor(r1)

    print(
        "Rezystancja zastępcza dla połączenia szeregowego:",
        (res1 + res2).get_resistance(),
    )
    print(
        "Rezystancja zastępcza dla połączenia równoległego:",
        (res1 | res2).get_resistance(),
    )


if __name__ == "__main__":
    main()
