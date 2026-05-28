
from abc import ABC, abstractmethod
import argparse
import numpy as np
import matplotlib.pyplot as plt

class Shape(ABC):
    def __init__(self, m):
        self.m = m  # Rozmiar macierzy (m x m)

    @abstractmethod
    def draw(self):
        """Zwraca macierz 2D reprezentującą kształt (używając np.fromfunction)."""
        pass


class Square(Shape):
    def __init__(self, m, a):
        super().__init__(m)
        self.a = a

    def draw(self):
        def condition(y, x):
            # ustawienie względem środka
            x0, y0 = x - self.m // 2, y - self.m // 2
            return (np.abs(x0) <= self.a / 2) & (np.abs(y0) <= self.a / 2)

        return np.fromfunction(condition, (self.m, self.m), dtype=int).astype(int)


class Rectangle(Shape):
    def __init__(self, m, a, b):
        super().__init__(m)
        self.a = a
        self.b = b

    def draw(self):
        def condition(y, x):
            x0, y0 = x - self.m // 2, y - self.m // 2
            return (np.abs(x0) <= self.a / 2) & (np.abs(y0) <= self.b / 2)

        return np.fromfunction(condition, (self.m, self.m), dtype=int).astype(int)


class Ellipse(Shape):
    def __init__(self, m, a, b):
        super().__init__(m)
        self.a = a
        self.b = b

    def draw(self):
        def condition(y, x):
            x0, y0 = x - self.m // 2, y - self.m // 2
            return (x0 / self.a) ** 2 + (y0 / self.b) ** 2 <= 1

        return np.fromfunction(condition, (self.m, self.m), dtype=int).astype(int)


def color_shape(shape_matrix, color, n):
    color_arr = np.array(color, dtype=float)
    background = np.zeros((*shape_matrix.shape, 3), dtype=float) # float, bo potem będziemy dzielić przez n^2
    image = np.where(shape_matrix[..., np.newaxis] == 1, color_arr, background)

    pad_w = n // 2
    
    smoothed = np.zeros_like(image, dtype=float)
    for dy in range(-pad_w, pad_w + 1):
        for dx in range(-pad_w, pad_w + 1):
            smoothed += np.roll(image, shift=(dy, dx), axis=(0, 1))
    smoothed /= (n ** 2)

    return np.clip(smoothed, 0, 255).astype(np.uint8) #cast do uint8, wówczas imshow poradzi sobie z renderowaniem RGB

def main():
    parser = argparse.ArgumentParser(description="Rysowanie kształtów w tablicy NumPy.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-s", "--square", type=float, metavar="A", help="Kwadrat o boku A"
    )
    group.add_argument(
        "-r",
        "--rectangle",
        type=float,
        nargs=2,
        metavar=("A", "B"),
        help="Prostokąt o wymiarach A i B",
    )
    group.add_argument(
        "-e",
        "--ellipse",
        type=float,
        nargs=2,
        metavar=("A", "B"),
        help="Elipsa o osiach A i B",
    )

    parser.add_argument(
        "-m", "--matrix-size", type=int, default=1000, help="Rozmiar macierzy (m x m)"
    )
    parser.add_argument(
        "-c",
        "--color",
        type=int,
        nargs=3,
        default=[255, 0, 0],
        metavar=("R", "G", "B"),
        help="Kolor RGB",
    )
    parser.add_argument(
        "-n",
        "--filter-size",
        type=int,
        default=3,
        help="Szerokość filtra wygładzającego",
    )

    args = parser.parse_args()

    if args.square is not None:
        shape = Square(args.matrix_size, args.square)
    elif args.rectangle is not None:
        shape = Rectangle(args.matrix_size, args.rectangle[0], args.rectangle[1])
    elif args.ellipse is not None:
        shape = Ellipse(args.matrix_size, args.ellipse[0], args.ellipse[1])

    matrix = shape.draw()

    colored_smoothed = color_shape(matrix, args.color, args.filter_size)

    # Dla macierzy 3D (M, M, 3) typu uint8 matplotlib automatycznie renderuje RGB, ignorując colormapy.
    plt.imshow(colored_smoothed)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
