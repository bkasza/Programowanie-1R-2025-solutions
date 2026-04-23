import sys


class Velocity:
    def __init__(self, beta: float = 0.0) -> None:
        """Inicjalizacja klasy

        Args:
            beta (float, optional): Prędkość w jednostce prędkości światła. Defaults to 0.0.
        """
        assert -1 < beta < 1, "Prędkość musi być w zakresie (-1, 1)"
        self.beta = beta

    def gamma(self) -> float:
        """Oblicza relatywistyczny czynnik gamma

        Returns:
            float: Wartość czynnika gamma
        """
        return 1 / (1 - self.beta**2) ** 0.5

    def __add__(self, other: "Velocity") -> "Velocity":
        """Przeciążenie operatora +
        Args:
            other (Velocity): Druga prędkość do dodania

        Returns:
            Velocity: Nowa prędkość będąca sumą relatywistyczną
        """
        new_beta = (self.beta + other.beta) / (1 + self.beta * other.beta)
        return Velocity(new_beta)

    def __iadd__(self, other: "Velocity") -> "Velocity":
        """Przeciążenie operatora +=, działamy na obiekcie self, aktualizując jego wartość beta

        Args:
            other (Velocity): Druga prędkość do dodania

        Returns:
            Velocity: Zaktualizowana prędkość będąca sumą relatywistyczną
        """
        self.beta = (self.beta + other.beta) / (1 + self.beta * other.beta)
        return self

    def __str__(self) -> str:
        """Reprezentacja tekstowa obiektu do printowania, zawierająca wartość beta i odpowiadający jej czynnik gamma

        Returns:
            str: Tekstowa reprezentacja obiektu
        """
        return f"beta = {self.beta:.6f},\ngamma = {self.gamma():.6f}"

    def __repr__(self) -> str:
        """Reprezentacja tekstowa obiektu do wywołania, zawierająca wartość beta i odpowiadający jej czynnik gamma

        Returns:
            str: Tekstowa reprezentacja obiektu
        """
        return f"beta = {self.beta:.6f},\ngamma = {self.gamma():.6f}"


def main():
    beta1 = Velocity(float(sys.stdin.readline()))
    beta2 = Velocity(float(sys.stdin.readline()))
    beta = beta1 + beta2
    print(beta)


if __name__ == "__main__":
    main()
