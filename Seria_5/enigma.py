from argparse import ArgumentParser

"""W tej imlementacji zwracam po raz pierwszy uwagę na predefiniowanie typów argumentów, co pozwala na lepszą czytelność kodu. 
Polega to na tym, że przy definicji funkcji określamy, jakiego typu argumenty przyjmuje i jaki typ zwraca. W ten sposób, gdy ktoś będzie czytał kod, od razu będzie wiedział, jakie dane są oczekiwane i jakie będą zwracane.
By zmusić interpeter należy włączyć opcję "type checking" w ustawieniach projektu. Wtedy, jeśli ktoś będzie próbował przekazać argumenty o niewłaściwym typie, otrzyma błąd już podczas uruchamiania programu, co pozwoli na szybsze wykrycie błędów.

Dodatkowo, zwracam uwagę na strukturę funkcji. Logika obliczania bitowej różnicy symetrycznej jest wydzielona, by pokazać, że operacja jest wspólna dla obu procesów, a logika zmienia się tylko w sposobie przetwarzania danych (znaki vs liczby). 
Dzięki temu, kod jest bardziej modularny i łatwiejszy do zrozumienia.

W kolejnym kroku będziemy chcieli dodać docstringi, by dodać czytelne opisy do funkcji.
"""

def bit_symmetric_difference(x: int, key: int) -> int:
    return x ^ key #XOR

def load_input_file(path, method: str) -> list:
    with open(path, 'r') as input_file:
        if method == 'e':
            return input_file.readlines()
        if method == 'd':
            return [line.split(' ') for line in input_file.readlines()]

def code_file(input_lines: list, output_file_path: str, key: int, method: str) -> None:
    with open(output_file_path, 'w') as output_file:
        if method == 'e':
            output_file.writelines(encrypt(input_lines, key))
        if method == 'd':
            output_file.writelines(decrypt(input_lines, key))

def encrypt(lines: list, key: int) -> list:
    return [
        ' '.join(str(bit_symmetric_difference(ord(ch), key)) for ch in line)
        for line in lines
    ]

def decrypt(lines: list, key: int) -> list:
    return [
        ''.join(chr(bit_symmetric_difference(int(num), key)) for num in line)
        for line in lines
    ]

def main() -> None:
    parser = ArgumentParser(description='Enigma coder/decoder')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the file')
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the file')
    parser.add_argument('key', type=int)
    parser.add_argument('--input_file_path', type = str, default = r"enigma_files\in.txt")
    parser.add_argument('--output_file_path', type = str, default = r"enigma_files\out.txt")    
    args = parser.parse_args()
    if args.encrypt:
        method = 'e'
    elif args.decrypt:
        method = 'd' 
    input_lines = load_input_file(args.input_file_path, method)
    code_file(input_lines, args.output_file_path, args.key, method)

if __name__ == '__main__':
    main()