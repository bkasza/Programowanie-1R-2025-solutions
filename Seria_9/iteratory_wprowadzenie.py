"generator umożliwia nam tworzenie iteratora, który generuje wartości na żądanie, zamiast przechowywać je wszystkie w pamięci. Przydatne jest to przy bardzo dużych zbiorach danych lub nieskończonych sekwencjach."


# %%
def count_up_to(n):
    yield "Zaczynamy liczenie!"
    count = 1
    while count <= n:
        yield count
        count += 1
    yield "Koniec liczenia!"


for number in count_up_to(5):
    print(number)

# %%


class CollatzIterator:
    """Iterator generujący kolejne liczby w ciągu Collatza, zaczynając od podanej liczby startowej"""

    def __init__(self, start):
        """Inicjalizacja iteratora z podaną liczbą startową."""
        self.current = start

    def __iter__(self):
        """Metoda zwracająca iterator"""
        return self

    def __next__(self):
        """Metoda zwracająca kolejny element ciągu Collatza lub sygnalizująca koniec iteracji."""
        if self.current == 0: 
            raise StopIteration

        result = self.current

        #żeby zwrócic 1 dodajemy wartosc zero, która zakonczy iteracje
        if self.current == 1:
            self.current = 0  
        elif self.current % 2 == 0:
            self.current //= 2
        else:
            self.current = 3 * self.current + 1

        return result


for number in CollatzIterator(5):
    print(number)
# %%
