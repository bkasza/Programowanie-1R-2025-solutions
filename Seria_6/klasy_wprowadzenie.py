# %%
"""
Zaczynamy przygodę z klasami, czyli obiektami, które łączą dane i funkcje operujące na tych danych.
"""

# Przypomnijmy sobie sprawdzanie typów

# %%

print(type("Hello"))
# %%
print(type(lambda x: x**2))
# %%
"""
Chcemy teraz utworzyć własny typ danych, własną strukturę.
"""

class Wojewodztwo:  # Definicja klasy, czyli naszego typu danych (nazwę zaczynamy zwyczajowo wielką literą)
    def __init__(self, nazwa: str, populacja: int):
        """
        Metoda specjalna (konstruktor), która jest wywoływana przy tworzeniu obiektu tej klasy, np. Wojewodztwo(...)
        """
        # "self" to odwołanie do konkretnego obiektu, który jest tworzony, czyli np. Wojewodztwo("śląskie", 5000000)
        self.nazwa = nazwa  # np. śląskie
        self.populacja = populacja  # np. 5000000

    def __str__(self) -> str:
        """
        Metoda specjalna, która jest wywoływana, gdy chcemy wypisać obiekt tej klasy (np. używając print)
        """
        return f"Województwo {self.nazwa} z populacją {self.populacja}"

    def __repr__(self) -> str:
        """
        Metoda specjalna, która jest wywoływana, gdy chcemy zobaczyć reprezentację tekstową obiektu tej klasy, np. repr(woj)
        """
        return f"Wojewodztwo(nazwa='{self.nazwa}', populacja={self.populacja})"


# %%
slaskie = Wojewodztwo("śląskie", 4600000)
# %%
print(type(slaskie))

# <class '__main__.Wojewodztwo'> # Oznacza, że jest to klasa Wojewodztwo zdefiniowana w obecnym pliku (w module __main__)
# %%

print(slaskie.nazwa)
print(slaskie.populacja)  # Odwołanie do atrybutów obiektu "slaskie"
# %%

print(slaskie)  # Niejawne wywołanie metody __str__() dla obiektu "slaskie"
# %%

""" 
Dodajmy do naszej definicji dodatkowe metody i atrybuty:
"""


class RozszerzoneWojewodztwo:
    def __init__(self, nazwa: str, populacja: int, stolica: str):
        self.nazwa = nazwa
        self.populacja = populacja
        self.stolica = stolica

    def __str__(self) -> str:
        return f"Województwo {self.nazwa} (stolica: {self.stolica}) z populacją {self.populacja}"

    def __repr__(self) -> str:
        return f"RozszerzoneWojewodztwo(nazwa='{self.nazwa}', populacja={self.populacja}, stolica='{self.stolica}')"

    def __call__(self) -> str:
        """
        Metoda specjalna, która pozwala na "wywołanie" obiektu tak jakby był funkcją.
        Przydatne, np. gdy chcemy, żeby nasz obiekt zachowywał się jak reguła, funkcja matematyczna lub akcja.
        """
        return f"Województwo {self.nazwa} zostało wywołane jak funkcja!"

    def _gestosc(self, a: int, b: int | float) -> float:
        """
        Przykładowa metoda prywatna, która jest przeznaczona tylko do użytku wewnętrznego w klasie.
        Nie jest dostępna dla użytkownika klasy, ale może być używana wewnątrz innych metod tej klasy.
        """
        return a / b

    def oblicz_gestosc_zaludnienia(self, powierzchnia: float) -> float:
        """
        Własna metoda (publiczna).
        Przyjmuje 'self' (czyli nasz bieżący obiekt) oraz dodatkowy argument 'powierzchnia'.
        """
        return self._gestosc(self.populacja, powierzchnia)


# %%
# Tworzymy nowy obiekt z pełnej klasy
slaskie_rozszerzone = RozszerzoneWojewodztwo("śląskie", 4500000, "Katowice")

print(slaskie_rozszerzone.stolica)  # Dostęp do zdefiniowanego atrybutu
print(slaskie_rozszerzone.oblicz_gestosc_zaludnienia(12333))  # Wywołanie własnej metody
print(slaskie_rozszerzone())  # Niejawne wywołanie metody __call__()
# %%

"""
Tradycyjny podział metod w Pythonie:
- metody specjalne (magiczne): np. __init__, __str__, __repr__, __call__ (wywoływane odpowiednimi operacjami wbudowanymi)
- metody publiczne: np. oblicz_gestosc_zaludnienia (dostępne dla użytkownika klasy)
- metody prywatne: np. z_oblicz_cos_wewnatrz (w przyjętej konwencji podłoga na początku oznacza metodę tylko do użytku wewnętrznego)
"""
# %%
