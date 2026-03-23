import matplotlib.pyplot as plt
from argparse import ArgumentParser
import bisect
from timeit import timeit

def przygotuj_histogram(granice, dane):
    """Przygotuj histogram z danych na podstawie podanych granic."""
    labels = [f"<{granice[0]}"] + \
             [f"{a}-{b}" for a,b in zip(granice[:-1], granice[1:])] + \
             [f">={granice[-1]}"]
    histogram = {label:0 for label in labels}
    for x in dane:
        "Najpierw sprawdzamy skrajne przedziały, a potem iterujemy po pozostałych."
        if x < granice[0]:
            histogram[labels[0]] += 1
            continue
        if x >= granice[-1]:
            histogram[labels[-1]] += 1
            continue
        for glow, gup in zip(granice[:-1], granice[1:]):
            "Zwróćcie uwagę, że taki zip daje nam od razu pary granic, więc nie musimy robić dodatkowych indeksów."
            if glow <= x < gup:
                histogram[f"{glow}-{gup}"] += 1
                break
    return histogram


def przygotuj_histogram_optymalny(granice, dane):
    """Okazuje się, że ten problem jest analogiczny do problemu wyszukiwania binarnego, więc możemy użyć funkcji bisect, która jest zoptymalizowana do tego typu zadań.
    W ten sposób uzyskujemy złożoność O(n log m), gdzie n to liczba danych, a m to liczba granic, co jest znacznie lepsze niż O(n*m) w przypadku poprzedniej implementacji.
    """

    labels = (
        [f"<{granice[0]}"] +
        [f"{a}-{b}" for a, b in zip(granice[:-1], granice[1:])] +
        [f">={granice[-1]}"]
    )
    histogram = {label: 0 for label in labels}
    for x in dane:
        "Bisect zwraca indeks, pod którym element x powinien być wstawiony, aby zachować porządek. W ten sposób możemy łatwo określić, do którego przedziału należy x."
        idx = bisect.bisect_left(granice, x) 
        histogram[labels[idx]] += 1
    return histogram

def narysuj_histogram(histogram):
    labels = list(histogram.keys())
    values = list(histogram.values())
    
    fig, ax = plt.subplots()
    ax.bar(labels, values) #alternatywnie plt.hist(dane, bins=granice) ale wtedy musimy podać dane i granice, a nie gotowy histogram
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_size(8)  
    plt.savefig("granice_plot\histogram.png")
    plt.show()

def wczytaj_dane_z_pliku():
    "Ważne jest, by wczytywać w konstrukcji with, ponieważ zapewnia to poprawne zamknięcie pliku po jego użyciu, nawet jeśli wystąpi błąd podczas odczytu."
    with open("D-42.json", "r") as f:
        import json
        data = json.load(f)
    return data["granice"], data["dane"]

def wczytaj_dane_z_argumentu():
    parser = ArgumentParser(description="Przygotuj histogram z danych.")
    parser.add_argument("--granice", nargs="+", type=float, required=True, help="Granice przedziałów")
    parser.add_argument("--dane", nargs="+", type=float, required=True, help="Dane do histogramu")
    args = parser.parse_args()
    return args.granice, args.dane

def main():
    granice, dane = wczytaj_dane_z_pliku()
    # granice, dane = wczytaj_dane_z_argumentu()
    histogram = przygotuj_histogram(granice, dane)
    print(timeit(lambda: przygotuj_histogram(granice, dane), number=10)) #teaser wykorzystania funkcji lambda i timeit
    print(timeit(lambda: przygotuj_histogram_optymalny(granice, dane), number=10))
    narysuj_histogram(histogram)

if __name__ == "__main__":
    main()
