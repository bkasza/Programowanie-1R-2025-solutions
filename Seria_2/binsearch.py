import argparse

"""krotka notka o wyszukiwaniu binarnym:
Wyszukiwanie binarne to algorytm służący do znajdowania pozycji określonego elementu w posortowanej liście (ważne!). 
Działa na zasadzie dzielenia listy na pół i porównywania szukanego elementu z elementem środkowym. 
Jeśli element środkowy jest równy szukanemu, zwraca jego indeks. 
Jeśli szukany element jest mniejszy niż element środkowy, algorytm kontynuuje wyszukiwanie w lewej połowie listy, a jeśli jest większy, to w prawej połowie. 
Proces ten powtarza się aż do znalezienia elementu lub stwierdzenia, że nie ma go w liście.
"""

def binary_search_iterative(element, lista, min_index, max_index):
    """Wyszukiwanie binarne iteracyjne"""
    lista = sorted(lista)
    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2
        if lista[mid_index] == element:
            print(f"Element {element} znaleziony na indeksie {mid_index}")
            return mid_index
        elif lista[mid_index] < element:
            min_index = mid_index + 1
        else:
            max_index = mid_index - 1
    print(f"Element {element} nie znaleziony w liście.")
    return -1

def binary_search_recursive(element, lista, min_index, max_index):
    """Wyszukiwanie binarne rekurencyjne"""
    lista = sorted(lista)
    if min_index > max_index:
        print(f"Element {element} nie znaleziony w liście.")
        return -1
    mid_index = (min_index + max_index) // 2
    if lista[mid_index] == element:
        print(f"Element {element} znaleziony na indeksie {mid_index}")
        return mid_index
    elif lista[mid_index] < element:
        return binary_search_recursive(element, lista, mid_index + 1, max_index)
    else:
        return binary_search_recursive(element, lista, min_index, mid_index - 1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Program do wyszukiwania binarnego")
    parser.add_argument('--element', type=int, help="Element do znalezienia")
    parser.add_argument("--list", nargs='+', type=int, help="Dowolna lista liczb", default=[1, 2, 3, 4, 5])
    parser.add_argument("--min", type=int, help="Indeks poczatkowy", default=0)
    parser.add_argument("--max", type=int, help="Indeks koncowy", default=4)
    args = parser.parse_args()
    # binary_search_iterative(args.element, args.list, args.min, args.max)
    binary_search_recursive(args.element, args.list, args.min, args.max)
    