#%%
"ostatnim aspektem klas który przeanalizujemy będzie dziedzczenie. weźmy przykład figur geometrycznych i obliczenia ich obwodów"

from abc import ABC, abstractmethod #ABC - abstract base class, abstractmethod - dekorator do oznaczania metod abstrakcyjnych

class Figure(ABC):
    """Generujemy klasę abstrakcyjną, która będzie bazą dla różnych figur geometrycznych."""
    @abstractmethod
    def circumference(self) -> float:
        """Obwód figury."""
        pass


class Circle(Figure):
    def __init__(self, x0: float, y0: float, r: float):
        self.x0 = x0
        self.y0 = y0
        self.r = r

    def circumference(self) -> float:
        from math import pi
        return 2 * pi * self.r
    
class Square(Figure):
    def __init__(self, x0: float, y0: float, a: float):
        self.x0 = x0
        self.y0 = y0
        self.a = a

    def circumference(self) -> float:
        return 4 * self.a
#%%
#abstract klasy nie da się utworzyć ze względu na abstract method

fig = Figure()

#%%
kolko = Circle(0, 0, 1)
print("Obwód koła", kolko.circumference())
kwadrat = Square(0, 0, 1)
print("Obwód kwadratu", kwadrat.circumference())
# %%

"Zastosowanie super()"

class Rectangle(Figure):
    def __init__(self, x0: float, y0: float, a: float, b: float):
        self.x0 = x0
        self.y0 = y0
        self.a = a
        self.b = b

    def circumference(self) -> float:
        return 2 * (self.a + self.b)
    
"Teraz zdefiniujmy Square z ogólnego czworokąta."
"Jako, że logika jest taka sama, możemy zdefiniować klasę Square2, która będzie dziedziczyć po Rectangle i będzie korzystać z jego metody circumference()"

class Square_2(Rectangle):
    def __init__(self, x0: float, y0: float, a: float):
        super().__init__(x0, y0, a, a)
        

sprytny_kwadrat = Square_2(0, 0, 5)
print("Obwód kwadratu:", sprytny_kwadrat.circumference())
# %%  
