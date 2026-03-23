from argparse import ArgumentParser


def caesar_cipher(text, shift):
    result = ""  # składamy wynik w tej zmiennej
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord("a")  # zamiana na kod ASCII dla 'a'
            else:
                base = ord("A")  # zamiana na kod ASCII dla 'A'
            result += chr(
                (ord(char) - base + shift_amount) % 26 + base
            )  # przesunięcie i zamiana z powrotem na znak
        else:
            result += char
    return result


def main():
    parser = ArgumentParser(description="Caesar Cipher")
    """Metoda z action umożliwia nam łatwe określenie, czy chcemy szyfrować czy odszyfrowywać tekst, bez konieczności ręcznego sprawdzania wartości argumentu tryb. 
    Jeżeli argument nie jest podany, to flaga ma wartość False, więc możemy łatwo obsłużyć ten przypadek w kodzie."""
    parser.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file') 
    """Możemy ustawić tryb jako argument pozycyjny, ale wtedy musimy ręcznie sprawdzać jego wartość, co jest mniej eleganckie."""
    # parser.add_argument(
    #     "--tryb",
    #     type=str,
    #     choices=["encrypt", "decrypt"],
    #     help="Wybierz tryb: encrypt lub decrypt",
    # )
    # if args.tryb == "encrypt":
    #     print(caesar_cipher(args.tekst, args.n))
    # else:
    #     print(caesar_cipher(args.tekst, -args.n)) #ten if oczywiscie powinien się znaleźć po parse_args.
    parser.add_argument("--tekst", type=str, help="Tekst do zaszyfrowania")
    parser.add_argument("-n", type=int, help="Liczba przesunięć")
    args = parser.parse_args()
    if args.encrypt:
        print(caesar_cipher(args.tekst, args.n))
    elif args.decrypt:
        print(caesar_cipher(args.tekst, -args.n))
    

if __name__ == "__main__":
    main()
