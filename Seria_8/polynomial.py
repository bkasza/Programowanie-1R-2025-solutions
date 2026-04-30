"""Zaczynamy zabawę z dziedziczeniem!
Najważniejsze założenie:
- mamy klasę matkę, która jest ogólnym przypadkiem
- mamy klasę dziecko, która jest szczególnym przypadkiem
- klasa dziecko dziedziczy po klasie matce, czyli przejmuje jej cechy i zachowania, ale może też mieć swoje własne cechy i zachowania, które są unikalne dla niej
- klasa dziecko może nadpisać (override) zachowania klasy matki, czyli zmienić sposób działania niektórych metod, które odziedziczyła po klasie matce

Dziedziczenie tworzymy przez podanie nazwy klasy matki w nawiasach po nazwie klasy dziecka.

Metoda super() pozwala nam odwołać się do klasy matki i wywołać jej metody, co jest szczególnie przydatne, gdy chcemy rozszerzyć funkcjonalność klasy matki, a nie całkowicie ją zastąpić.
"""


from sympy import hermite, legendre, Poly, Symbol
from argparse import ArgumentParser


'uwaga, mi zadziałało z all_coeffs, żeby dostać wszystkie współczynniki'
def HermiteCoefficients(n):
    x = Symbol("x")
    return Poly(hermite(n, x), x).all_coeffs()[::-1] # aby szło od najniższego stopnia do najwyższego


def LegendreCoefficients(n):
    x = Symbol("x")
    return Poly(legendre(n, x), x).all_coeffs()[::-1]


class Polynomial:
    c = []

    def __init__(self, c: list[float]) -> None:
        """Lista współczynników w konwencji W(x) = c[0]+c[1]*x+c[2]*x^2+...+c[n]*x^n

        Args:
            c (list[float]): Lista współczynników wielomianu.
        """
        self.c = c

    def deg(self):
        return len(self.c) - 1

    def __getitem__(self, index: int) -> float:
        """Metoda [] do pobierania wartości współczynnika wielomianu.

        Args:
            index (int): Indeks współczynnika, który chcemy sprawdzić (odczytać).

        Returns:
            float: Wartość współczynnika o podanym indeksie.
        """

        return self.c[index]

    def __setitem__(self, index: int, value: float) -> None:
        """Metoda [] do ustawiania wartości współczynnika wielomianu.

        Args:
            index (int): Indeks współczynnika, który chcemy zmienić.
            value (float): Nowa wartość współczynnika o podanym indeksie.
        """

        self.c[index] = value

    def __call__(self, x: float) -> float:
        """Policz W(x) dla podanego x.

        Args:
            x (float): Wartość, dla której chcemy obliczyć wartość wielomianu.

        Returns:
            float: Wartość wielomianu dla podanego x.
        """

        return sum(c * (x**i) for i, c in enumerate(self.c))

    def __mul__(self, real: float) -> "Polynomial":
        """Mnożenie wielomianu przez liczbę rzeczywistą.

        Args:
            real (float): Liczba rzeczywista, przez którą chcemy pomnożyć wielomian.

        Returns:
            Polynomial: Nowy wielomian, który jest wynikiem mnożenia.
        """

        return Polynomial([c * real for c in self.c])

    def __rmul__(self, real: float) -> "Polynomial":
        """Mnożenie liczby rzeczywistej przez wielomian (odwrotna kolejność)."""
        return self.__mul__(real)

    def __add__(self, other: "Polynomial") -> "Polynomial":
        """Dodawanie dwóch wielomianów, sprowadza się do dodawania współczynnikówo tych samych stopniach

        Args:
            other (Polynomial): Drugi wielomian.

        Returns:
            Polynomial: Nowy wielomian, który jest wynikiem dodawania.
        """
        higher_order_poly = self if self.deg() >= other.deg() else other
        lower_order_poly = self if self.deg() < other.deg() else other
        new_coefficients = higher_order_poly.c.copy()
        for i in range(lower_order_poly.deg() + 1):
            new_coefficients[i] += lower_order_poly[i]
        return Polynomial(new_coefficients)
    
    def __str__(self) -> str:
        """Reprezentacja tekstowa wielomianu

        Returns:
            str: Reprezentacja tekstowa wielomianu.
        """

        return " + ".join(f"{c}*x^{i}" for i, c in enumerate(self.c) if c != 0) or "0"

    @property
    def d(self) -> "Polynomial":
        """Pochodna wielomianu.

        Returns:
            Polynomial: Pochodna 1 stopnia wielomianu.
        """
        n = 1
        new_coefficients = self.c.copy()
        for _ in range(n):
            new_coefficients = [i * c for i, c in enumerate(new_coefficients)][1:]
        return Polynomial(new_coefficients)


class HermitePolynomial(Polynomial):
    def __init__(self, n: int) -> None:
        """Inicjalizacja wielomianu Hermite'a stopnia n.

        Args:
            n (int): Stopień wielomianu Hermite'a.
        """
        super().__init__(HermiteCoefficients(n))


class LegendrePolynomial(Polynomial):
    def __init__(self, n: int) -> None:
        """Inicjalizacja wielomianu Legendre'a stopnia n.

        Args:
            n (int): Stopień wielomianu Legendre'a.
        """
        super().__init__(LegendreCoefficients(n))


expressions_to_test = [
    lambda Hn, Ln, x: Hn(x),
    lambda Hn, Ln, x: Ln(x),
    lambda Hn, Ln, x: Hn.d(x) + Ln.d(x) + 3 * (Hn(x) + Ln(x)),
]



def main():
    parser = ArgumentParser(description="Wielomiany Hermite'a i Legendre'a ")
    parser.add_argument("n", type=int, help="Stopień wielomianów")
    parser.add_argument("x", type=float, help="Zmienna dla której obliczamy wartość")
    args = parser.parse_args()
    Hn = HermitePolynomial(args.n)
    Ln = LegendrePolynomial(args.n)
    for i, expr in enumerate(expressions_to_test):
        print(f"Expression {i+1}: {expr(Hn, Ln, args.x)}")


if __name__ == "__main__":
    main()
