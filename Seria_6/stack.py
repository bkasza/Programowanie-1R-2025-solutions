from argparse import ArgumentParser

# Zabawa w symulowanie cpp w pythonie: https://www.geeksforgeeks.org/cpp/stack-in-cpp-stl/


class Stack:
    def __init__(self) -> None:
        self._stack: list[float] = []

    def push(self, item: float) -> None:
        self._stack.append(item)

    def pop(self) -> float:
        if not self.is_empty():
            return self._stack.pop()
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        return len(self._stack) == 0


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="Lista liczb zmiennoprzecinkowych do umieszczenia na stosie",
    )
    args = parser.parse_args()

    stack = Stack()
    for number in args.numbers:
        stack.push(number)

    while not stack.is_empty():
        print(
            stack.pop(), end=" "
        )  # dzięki end=" " wypisujemy liczby w jednej linii, oddzielone spacją


if __name__ == "__main__":
    main()
