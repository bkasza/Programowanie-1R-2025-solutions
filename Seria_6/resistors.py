import sys

# pokazać jak szybko generować docstringi z autoDocstring - Python Docstring Generator


class Resistor:
    def __init__(self, resistance: float = 0):
        """Inicjalizacja klasy Resistor, która reprezentuje rezystor elektryczny. Przyjmuje opcjonalny argument resistance, który określa wartość rezystancji. Domyślnie jest ustawiona na 0.

        Args:
            resistance (float, optional): Wartość oporu opornika. Defaults to 0.
        """

        # Wcześniej poznaliśmy jedną podłogę (np. _nazwa), która była tylko "umową" (konwencją) nieużywania atrybutu.
        # Tutaj celowo używamy dwóch podłóg (__R). Włącza to mechanizm tzw. "name mangling", który
        # w locie zmienia nazwę atrybutu, silnie blokując do niego dostęp z zewnątrz.
        # Robimy to, by wymusić na użytkowniku używanie naszych metod: get_resistance() i set_resistance()
        self.__R = resistance

    # @property jako ciekawy sposób na stworzenie getterów i setterów, ale nie jest to konieczne, więc zostawiamy to jako ciekawostkę
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


def series(a: Resistor, b: Resistor) -> Resistor:
    """Funkcja zewnętrzna series oblicza rezystancję zastępczą dla dwóch rezystorów połączonych szeregowo.

    Args:
        a (Resistor): Pierwszy rezystor
        b (Resistor): Drugi rezystor

    Returns:
        Resistor: Rezystor o rezystancji zastępczej
    """
    return Resistor(a.get_resistance() + b.get_resistance())


def parallel(a: Resistor, b: Resistor) -> Resistor:
    """Funkcja zaprzyjaźniona parallel oblicza rezystancję zastępczą dla dwóch rezystorów połączonych równolegle.
    Ponieważ Python nie posiada mechanizmu funkcji zaprzyjaźnionych jak C++, w tej
    sytuacji odwołujemy się wprost do atrybutów prywatnych za pomocą mechanizmu "name mangling",
    podczas gdy funkcja series używa publicznych metod get_resistance().
    Args:
        a (Resistor): Pierwszy rezystor
        b (Resistor): Drugi rezystor

    Raises:
        ValueError: Jeśli którykolwiek z rezystorów ma rezystancję równą zero, co jest niedozwolone w połączeniu równoległym.

    Returns:
        Resistor: Rezystor o rezystancji zastępczej
    """
    # uwaga, zawołanie a.__R nie zadziała!
    if (
        a._Resistor__R == 0 or b._Resistor__R == 0
    ):  # name mangling zmienia nazwę __R na _Resistor__R, więc musimy użyć tej formy, by się do niego odwołać
        raise ValueError(
            "Rezystancja nie może być równa zero w połączeniu równoległym."
        )
    return Resistor(1 / (1 / a._Resistor__R + 1 / b._Resistor__R))


def main() -> None:
    """Wczytujemy ze standardowego wejścia dwie wartości oporu rezystorów. Zwracamy wartość oporu zastępczego dla połączenia równoległego i szeregowego."""
    r0 = float(sys.stdin.readline())
    r1 = float(sys.stdin.readline())
    res1 = Resistor(r0)
    res2 = Resistor(r1)
    print(
        "Rezystancja zastępcza dla połączenia szeregowego:",
        series(res1, res2).get_resistance(),
    )
    print(
        "Rezystancja zastępcza dla połączenia równoległego:",
        parallel(res1, res2).get_resistance(),
    )


# Przypomnienie o co chodzi z __main__:
# Jeśli nasz plik plik jest uruchamiany bezpośrednio z terminala (np. python3 resistors.py), to funkcja main() zostanie wywołana,
# a program będzie oczekiwał na wprowadzenie dwóch wartości oporu rezystorów.
# Jeśli jednak ten plik jest przez kogoś importowany jako moduł do innego skryptu (np. `import resistors`),
# to blok if się NIE wykonana (zmienna ukryta __name__ będzie miała inną nazwę) i funkcja main() nie zostanie automatycznie wywołana.
# Pozwala to na ładne dzielenie się napisanymi w tym pliku klasą i metodami, bez martwienia się,
# że wymuszą one od razu wejście sys.stdin na importującym kodzie.
if __name__ == "__main__":
    main()
