# %%
"""
W tej serii zadaniowej pojawi się zagadnienie operowania na instancjach klas z wykorzystaniem operatorów takich jak +, *, +=
"""


class Point:
    """Za przykład weźmiemy klasę punktu na przestrzenii euklidesowej."""

    def __init__(self, x0: float, y0: float) -> None:
        """Inicjalizacja punktu

        Args:
            x0 (float): x0
            y0 (float): y0
        """
        self.x0 = x0
        self.y0 = y0

    def __add__(self, other: "Point") -> "Point":
        """Dodawanie dwóch punktów. Wywołanie: punkt1 + punkt2

        Args:
            other (Point): Drugi punkt, który chcemy dodać do pierwszego.

        Returns:
            Point: Nowy punkt, który jest wynikiem dodawania. Zwracana jest !NOWA! instancja klasy Point.
        """
        return Point(self.x0 + other.x0, self.y0 + other.y0)

    def __mul__(self, scalar: float) -> "Point":
        """Mnożenie lewostronnne punktu przez skalar. Wywołanie: punkt * float

        Args:
            scalar (float): Liczba rzeczywista, przez którą chcemy pomnożyć punkt.

        Returns:
            Point: Nowy punkt, który jest wynikiem mnożenia. Zwracana jest !NOWA! instancja klasy Point.
        """
        return Point(self.x0 * scalar, self.y0 * scalar)

    def __rmul__(self, scalar: float) -> "Point":
        """Mnożenie prawostronne skalaru przez punkt (odwrotna kolejność). Wywołanie: float * punkt"""
        return self.__mul__(scalar)

    def __iadd__(self, other):
        """Dodawanie dwóch punktów z modyfikacją pierwszego. Wywołanie: punkt1 += punkt2

        Args:
            other (Point): Drugi punkt, który chcemy dodać do pierwszego.

        Returns:
            Point: Zmodyfikowany pierwszy punkt, który jest wynikiem dodawania. Zwracana jest !TA SAMA! instancja klasy Point.
        """
        self.x0 += other.x0
        self.y0 += other.y0
        return self

    def __str__(self) -> str:
        return f"Point({self.x0}, {self.y0})"


# %%
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3)
# %%
p4 = p1 * 2
print(p4)

# %%
p5 = 2 * p1
print(p5)

# %%
p1 += p2
print(p1 += p2)
# wywołaj pare razy
# %%

"""Pozostałe metody specjalne, które się mogą nam przydać
/ : __truediv__(self, other) #dzielenie przez other

-= : __isub__(self, other) #odejmowanie other, modyfikujące self
*= : __imul__(self, other) #mnożenie przez other, modyfikujące self
/= : __itruediv__(self, other) #dzielenie przez other, modyfikujące self

- : __neg__(self) #negacja zwracają nową instancję

== : __eq__(self, other)
!= : __ne__(self, other)
"""
