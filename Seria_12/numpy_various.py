
import argparse

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
