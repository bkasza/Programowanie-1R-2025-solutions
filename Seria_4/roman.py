from argparse import ArgumentParser

int_to_romans_dict = {
    1000:"M",
    900:"CM",
    500:"D",
    400:"CD",
    100:"C",
    90:"XC",
    50:"L",
    40:"XL",
    10:"X",
    9:"IX",
    5:"V",
    4:"IV",
    1:"I"
}

romans_to_int_dict = {v:k for k,v in int_to_romans_dict.items()}

def integer_to_roman(int_num):
    """Konwersja liczby całkowitej na rzymską polega na iteracji po posortowanym słowniku int_to_romans_dict i dopóki liczba całkowita jest większa lub równa aktualnej wartości,
    dodajemy odpowiadający symbol do wyniku i odejmujemy tę wartość od liczby całkowitej.
    Krytyczne jest to, by słownik był posortowany.
    """
    assert 0 < int_num < 4000, "Liczba musi być pomiędzy 1 and 3999"
    result = ""
    for value, symbol in int_to_romans_dict.items():
    # wszystko zasadza się na posortowanym słowniku
        while int_num >= value:
            result += symbol
            int_num -= value

    return result

def roman_to_integer(roman_num):
    """Konwersja liczby rzymskiej na całkowitą polega na iteracji po znakach liczby rzymskiej i sumowaniu odpowiadających im wartości."""
    result = 0
    i = 0
    n = len(roman_num)

    while i < n:
        if i+1 < n and romans_to_int_dict[roman_num[i]] < romans_to_int_dict[roman_num[i+1]]:
            result += romans_to_int_dict[roman_num[i+1]] - romans_to_int_dict[roman_num[i]]
            i += 2
        else:
            result += romans_to_int_dict[roman_num[i]]
            i += 1

    return result

def main():
    parser = ArgumentParser(description="Konwerter liczb rzymskich i arabskich")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-a", "--arabic", type=int, help="Liczba całkowita do konwersji na rzymską")
    group.add_argument("-r", "--roman", type=str, help="Liczba rzymska do konwersji na całkowitą")

    args = parser.parse_args()

    if args.arabic is not None:
        print(f"{args.arabic}: {integer_to_roman(args.arabic)}")
    else:
        print(f"{args.roman}: {roman_to_integer(args.roman)}")

if __name__ == "__main__":
    main()