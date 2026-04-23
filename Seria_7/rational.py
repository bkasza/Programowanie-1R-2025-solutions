import sys


class RationalNumber:
    def __init__(self, p: int = 0, q: int = 1):
        """Konstruktor klasy RationalNumber, który inicjalizuje licznik p i mianownik q.

        Args:
            p (int, optional): Licznik. Defaults to 0.
            q (int, optional): Mianownik. Defaults to 1.
        """
        if q == 0:
            raise ZeroDivisionError("Mianownik nie może być zerem.")
        self.p = p
        self.q = q
        self._reduce()

    def _gcd(self, a: int, b: int) -> int:
        """Algorytm Euklidesa do obliczania największego wspólnego dzielnika

        Args:
            a (int): Licznik
            b (int): Mianownik

        Returns:
            int: Największy wspólny dzielnik
        """
        while b:
            a, b = b, a % b
        return abs(a)

    def _reduce(self):
        if self.q < 0:
            self.p = -self.p
            self.q = -self.q
        gcd = self._gcd(self.p, self.q)
        self.p //= gcd
        self.q //= gcd

    # kusi tu zrobić @property
    def numerator(self) -> int:
        """Zwracamy licznik

        Returns:
            int: Licznik
        """
        return self.p

    def denominator(self) -> int:
        """Zwracamy mianownik

        Returns:
            int: Mianownik
        """
        return self.q

    def __float__(self) -> float:
        """Metoda specjalna do obliczenia reprezentacji zmiennoprzecinkowej.

        Returns:
            float: Reprezentacja zmiennoprzecinkowa liczby wymiernej
        """
        return self.p / self.q

    def __neg__(self):
        """Metoda specjalna do obliczenia przeciwieństwa liczby wymiernej."""
        return RationalNumber(-self.p, self.q)  # neg ma zwracać nową instancję

    def __lt__(self, other: "RationalNumber") -> bool:
        """ "
        Metoda specjalna do porównania "p1/q1<p2/q2" dwóch liczb wymiernych.
        Ponieważ p1/q1 < p2/q2 jest równoważne dla p1*q2 < p2*q1, możemy porównać iloczyny bez konieczności
        konwersji do float, co pozwala uniknąć problemów z precyzją.

        Args:
            other (RationalNumber): Liczba do porównania

        Returns:
            bool: _description_
        """
        return self.p * other.denominator() < other.numerator() * self.q

    def __add__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania sumy liczb wymiernych.

        Args:
            other (RationalNumber): Liczba do dodania

        Returns:
            RationalNumber: Liczba wymierna będąca sumą self i other
        """

        new_denominator = self.q * other.denominator()
        new_numerator = self.p * other.denominator() + other.numerator() * self.q
        return RationalNumber(new_numerator, new_denominator)

    def __sub__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania różnicy liczb wymiernych.

        Args:
            other (RationalNumber): Liczba do odjęcia

        Returns:
            RationalNumber: Liczba wymierna będąca różnicą self i other
        """
        new_denominator = self.q * other.denominator()
        new_numerator = self.p * other.denominator() - other.numerator() * self.q
        return RationalNumber(new_numerator, new_denominator)

    def __mul__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania iloczynu liczb wymiernych.

        Args:
            other (RationalNumber): Liczba do pomnożenia

        Returns:
            RationalNumber: Liczba wymierna będąca iloczynem self i other
        """
        new_numerator = self.p * other.numerator()
        new_denominator = self.q * other.denominator()
        return RationalNumber(new_numerator, new_denominator)

    def __truediv__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania ilorazu liczb wymiernych.

        Args:
            other (RationalNumber): Liczba do podzielenia

        Returns:
            RationalNumber: Liczba wymierna będąca ilorazem self i other
        """
        new_numerator = self.p * other.denominator()
        new_denominator = self.q * other.numerator()
        return RationalNumber(new_numerator, new_denominator)

    def __iadd__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania sumy liczb wymiernych i przypisania wyniku do self.

        Args:
            other (RationalNumber): Liczba do dodania

        Returns:
            RationalNumber: Liczba wymierna będąca sumą self i other, przypisana do self
        """
        new_denominator = self.q * other.denominator()
        new_numerator = self.p * other.denominator() + other.numerator() * self.q
        self.p = new_numerator
        self.q = new_denominator
        self._reduce()
        return self

    def __isub__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania różnicy liczb wymiernych i przypisania wyniku do self.

        Args:
            other (RationalNumber): Liczba do odjęcia

        Returns:
            RationalNumber: Liczba wymierna będąca różnicą self i other, przypisana do self
        """
        new_denominator = self.q * other.denominator()
        new_numerator = self.p * other.denominator() - other.numerator() * self.q
        self.p = new_numerator
        self.q = new_denominator
        self._reduce()
        return self

    def __imul__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania iloczynu liczb wymiernych i przypisania wyniku do self.

        Args:
            other (RationalNumber): Liczba do pomnożenia

        Returns:
            RationalNumber: Liczba wymierna będąca iloczynem self i other, przypisana do self
        """
        new_numerator = self.p * other.numerator()
        new_denominator = self.q * other.denominator()
        self.p = new_numerator
        self.q = new_denominator
        self._reduce()
        return self

    def __itruediv__(self, other: "RationalNumber") -> "RationalNumber":
        """Metoda specjalna do obliczania ilorazu liczb wymiernych i przypisania wyniku do self.

        Args:
            other (RationalNumber): Liczba do podzielenia

        Returns:
            RationalNumber: Liczba wymierna będąca ilorazem self i other, przypisana do self
        """
        new_numerator = self.p * other.denominator()
        new_denominator = self.q * other.numerator()
        self.p = new_numerator
        self.q = new_denominator
        self._reduce()
        return self

    def __repr__(self) -> str:
        return f"RationalNumber({self.p}, {self.q})"

    def __str__(self) -> str:
        if self.q == 1:
            return str(self.p)
        return f"{self.p}/{self.q}"


def main():
    data = sys.stdin.readline().split()
    if len(data) < 2:
        return
    "Działa przy założeniu podania dwóch liczb wymiernych w formacie p/q, oddzielonych spacją + Enter"

    p1_str, q1_str = data[0].split("/")
    p2_str, q2_str = data[1].split("/")

    r1 = RationalNumber(int(p1_str), int(q1_str))
    r2 = RationalNumber(int(p2_str), int(q2_str))

    # reprezentacja dziesietna .g usuwa zera
    print(f"{float(r1):.6g} {float(r2):.6g}")

    # liczby przeciwne do podanych
    print(f"{-r1} {-r2}")

    # kolejnośc niemalejąca (dzięki implementacji __lt__ możemy użyć sortowania)
    r_min, r_max = sorted([r1, r2])
    print(f"{r_min} {r_max}")

    # suma i iloczyn
    print(f"{r1 + r2} {r1 * r2}")


if __name__ == "__main__":
    main()
