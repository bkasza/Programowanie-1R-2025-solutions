from argparse import ArgumentParser


def check_brackets(brackets):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for char in brackets:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if len(stack) == 0:
                return False
            else:
                top = stack.pop()
            if pairs[char] != top:
                return False
        else:
            raise ValueError(f"Nieobsługiwany znak: {char}")
    return len(stack) == 0


def count_missing_parentheses(brackets):
    open_count = 0
    missing_count = 0
    for char in brackets:
        if char == "(":
            open_count += 1
        elif char == ")":
            if open_count > 0:
                open_count -= 1
            else:
                missing_count += 1
    return missing_count + open_count


def generate_balanced_parentheses(n):
    """Wyjaśnienie rekurencji raz jeszcze:
    1. Ciąg wyrazów jest generowany poprzez dodawanie nawiasów do aktualnego ciągu.
    2. Jeśli liczba otwartych nawiasów jest mniejsza niż n, możemy dodać kolejny otwarty nawias.
    3. Jeśli liczba zamkniętych nawiasów jest mniejsza niż liczba otwartych, możemy dodać zamknięty nawias.
    4. Proces ten jest powtarzany aż do momentu, gdy długość aktualnego ciągu osiągnie 2*n, co oznacza, że mamy n par nawiasów.
    5. Każdy wygenerowany ciąg jest dodawany do wyniku, który jest zwracany na końcu.
    6. Przypadek dla dwóch nawiasów:
    - Start: current="", left=0, right=0
    - Dodajemy "(": current="(", left=1, right=0
    - Dodajemy "(": current="((", left=2, right=0 -- wyczerpalismy lewą stronę
    - Dodajemy ")": current="(()", left=2, right=1 
    - Dodajemy ")": current="(())", left=2, right=2 -- gotowy ciąg, dodajemy do wyniku
    - Wracamy do current="(", left=1, right=0 i dodajemy ")": current="()", left=1, right=1, bo wykonaliśmy pierwszy if statement, ale możemy jeszcze dodać zamknięty nawias
    - Dodajemy "(": current="()(", left=2, right=1
    - Dodajemy ")": current="()()", left=2, right=2 -- gotowy ciąg, dodajemy do wyniku
    - Ostatecznie wynik to ["(())", "()()"]
    """
    result = []
    # istotna rekurencja, która generuje wszystkie możliwe kombinacje nawiasów
    def generator(current="", left=0, right=0):
        if len(current) == 2 * n:
            result.append(current)
            return
        if left < n:
            generator(current + "(", left + 1, right)
        #kiedy wyczerpiemy wszystkie lewe strony idziemy do prawej
        if right < left:
            generator(current + ")", left, right + 1)

    generator()
    return result


def main():
    parser = ArgumentParser(description="Brackets")
    parser.add_argument(
        "tryb",
        type=str,
        choices=["check", "fix", "list"],
        help="Wybierz tryb: check, fix lub list",
    )
    parser.add_argument("argument", type=str, help="Argument dla wybranego trybu")
    args = parser.parse_args()
    if args.tryb == "check":
        print(check_brackets(args.argument))
    elif args.tryb == "fix":
        print(count_missing_parentheses(args.argument))
    elif args.tryb == "list":
        n = int(args.argument)
        print(generate_balanced_parentheses(n))


if __name__ == "__main__":
    main()

# example usage:
# python brackets.py check "(()[]){}"
# python brackets.py fix "(())))))))))(((("
# python brackets.py list 3
