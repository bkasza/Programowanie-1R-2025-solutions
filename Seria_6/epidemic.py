from argparse import ArgumentParser
from random import random, uniform
import matplotlib.pyplot as plt
from math import cos, sin, pi
import matplotlib.animation as animation


def step_counter(method):
    """
    Dekorator zliczający wywołania metody.
    Wykorzystuje parametr `self`, aby przypisać licznik bezpośrednio do instancji
    obiektu, dzięki czemu każdy obiekt ma swój własny, niezależny licznik.
    """

    def wrapper(self, *args, **kwargs):
        # Sprawdź, czy instancja ma już atrybut licznika; jeśli nie, utwórz go
        if not hasattr(self, "_step_counter"):
            self._step_counter = 0
        self._step_counter += 1
        # Wywołaj oryginalną metodę, przekazując self i resztę argumentów
        return method(self, *args, **kwargs)

    return wrapper


class Person:
    def __init__(self, x: float, y: float, status: str):
        self.x = x
        self.y = y
        self.status = status

    MaxDistance = 5.0
    MaxIllDistance = 0.5

    def Move(self):
        if self.status == "healthy":
            distance = uniform(0, Person.MaxDistance)  # wylosuj odległość ruchu
        else:
            distance = uniform(0, Person.MaxIllDistance)

        angle = uniform(0, 2 * pi)  # wylosuj kierunek ruchu
        dx = distance * cos(angle)
        dy = distance * sin(angle)

        self.x += dx
        self.y += dy

    def Info(self) -> str:
        return f"Status: {self.status}, Position: ({self.x:.2f}, {self.y:.2f})"

    def __str__(self) -> str:
        return self.Info()


class Population:
    InfectionProbability = 0.2
    InfectionDistance = 1.0

    def __init__(self, w: float, h: float, population_size: int):
        self.w = w
        self.h = h
        self.people: list[Person] = []
        self.history_healthy: list[int] = []
        self.history_infected: list[int] = []
        self.history_carrier: list[int] = []

        for _ in range(population_size):
            x = uniform(0, w)
            y = uniform(0, h)
            if random() < self.InfectionProbability:
                if random() < 0.5:
                    status = "infected"
                else:
                    status = "carrier"
            else:
                status = "healthy"
            self.people.append(Person(x, y, status))

        self._record_stats()

    def _record_stats(self):
        healthy = sum(1 for p in self.people if p.status == "healthy")
        infected = sum(1 for p in self.people if p.status == "infected")
        carrier = sum(1 for p in self.people if p.status == "carrier")
        self.history_healthy.append(healthy)
        self.history_infected.append(infected)
        self.history_carrier.append(carrier)

    def move(self):
        for person in self.people:
            person.Move()
            person.x %= self.w  # periodyczne warunki brzegowe
            person.y %= self.h

        # Tworzymy cache infekujących i poppowanych - wydzielone dla przejrzystości list comprehensions
        infectious_people = [
            p for p in self.people if p.status in ("infected", "carrier")
        ]
        healthy_people = [p for p in self.people if p.status == "healthy"]

        for healthy in healthy_people:
            for sick in infectious_people:
                dist = ((healthy.x - sick.x) ** 2 + (healthy.y - sick.y) ** 2) ** 0.5
                if dist < self.InfectionDistance:
                    if random() < self.InfectionProbability:
                        healthy.status = "infected" if random() < 0.5 else "carrier"
                        break  # bo zdrowa osoba może zostać zainfekowana tylko raz

        self._record_stats()

    plot_data = {
        "healthy": {"color": "blue", "marker": "o"},
        "infected": {"color": "red", "marker": "X"},
        "carrier": {"color": "orange", "marker": "*"},
    }

    @step_counter
    def paint(self):
        plt.clf()

        for person in self.people:
            plt.scatter(
                person.x,
                person.y,
                color=self.plot_data[person.status]["color"],
                marker=self.plot_data[person.status]["marker"],
                alpha=0.6,
            )
        plt.xlim(0, self.w)
        plt.ylim(0, self.h)
        step = getattr(self, "_step_counter", 0)
        plt.title(f"Symulacja epidemii (Krok: {step})")
        plt.xlabel("X")
        plt.ylabel("Y")

    def save_stats_plot(self, filename: str):
        plt.figure()
        plt.plot(self.history_healthy, label="Healthy", color="blue", linewidth=2)
        plt.plot(self.history_infected, label="Infected", color="red", linewidth=2)
        plt.plot(self.history_carrier, label="Carrier", color="orange", linewidth=2)
        plt.title("Statystyki populacji podczas epidemii")
        plt.xlabel("Krok symulacji")
        plt.ylabel("Liczba osób")
        plt.legend()
        plt.savefig(filename)
        plt.close()


def animation_frame(frame, population: Population):
    population.move()
    population.paint()


def create_animation(population: Population, steps: int, gif_path: str):
    fig = plt.figure()
    anim = animation.FuncAnimation(
        fig,
        animation_frame,# type: ignore
        fargs=(population,),
        frames=steps,
        repeat=True,  
    )
    anim.save(gif_path, writer="imagemagick", fps=5)


def run_simulation(
    w: float,
    h: float,
    population_size: int,
    steps: int,
    gif_path: str | None = None,
    stats_plot_path: str | None = None,
):
    population = Population(w, h, population_size)
    if gif_path is not None:
        create_animation(population, steps, gif_path)
    else:
        for _ in range(steps):
            population.move()
            population.paint()
            plt.pause(0.1)
        plt.close()  # zamykamy okno po symulacji w pętli

    if stats_plot_path:
        population.save_stats_plot(stats_plot_path)


def main():
    parser = ArgumentParser(description="Symulacja epidemii w populacji.")
    parser.add_argument(
        "--width", type=float, default=50, help="Szerokość obszaru symulacji"
    )
    parser.add_argument(
        "--height", type=float, default=50, help="Wysokość obszaru symulacji"
    )
    parser.add_argument(
        "--population", type=int, default=50, help="Liczba osób w populacji"
    )
    parser.add_argument(
        "--steps", type=int, default=100, help="Liczba kroków symulacji"
    )
    parser.add_argument(
        "--gif_path",
        type=str,
        default=r"epidemic_plots\symulacja.gif",
        # default=None,
        help="Ścieżka do zapisu animacji GIF",
    )
    parser.add_argument(
        "--stats_plot_path",
        type=str,
        default=r"epidemic_plots\statystyka.png",
        help="Ścieżka do zapisu statystyki",
    )
    args = parser.parse_args()

    run_simulation(
        args.width,
        args.height,
        args.population,
        args.steps,
        args.gif_path,
        args.stats_plot_path,
    )


if __name__ == "__main__":
    main()
