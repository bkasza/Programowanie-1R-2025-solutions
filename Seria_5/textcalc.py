from argparse import ArgumentParser

"""W tym zadaniu zależało mi głównie na implementacji wyboru operacji matematycznej. 
Korzystamy z funkcji lambda, którą możemy przypisać do klucza w słowniku, co pozwala nam na łatwe mapowanie operatorów na odpowiednie funkcje.

Dodatkowo, w funkcji eval_trick pokazuję, jak można wykorzystać funkcję eval do wykonania bardziej skomplikowanych operacji matematycznych, takich jak potęgowanie.
Funkcja eval przyjmuje string i interpretuje go jako kod Pythona, co pozwala nam na wykonanie operacji matematycznych bez konieczności ręcznego mapowania operatorów.
Oczywiście, korzystanie z eval może być niebezpieczne, jeśli nie mamy kontroli nad tym, co jest przekazywane do tej funkcji, dlatego w tym przypadku jest to tylko przykład i nie zalecam używania eval w praktycznych zastosowaniach bez odpowiednich zabezpieczeń.
Przykładem jest potęgowanie, gdzie musimy zastąpić operator '^' na '**', ponieważ w Pythonie operator '^' oznacza XOR, a nie potęgowanie.
"""
operation_dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a ** b,
    '%': lambda a, b: a % b,
}

def load_input(path: str):
    with open(path, 'r') as grocery_list:
        return grocery_list.readlines()

def eval_calculation(instruction_line):
    a, sign, b = instruction_line.strip().split(" ")
    a, b = float(a), float(b)
    return operation_dict[sign](a, b)

def eval_trick(instruction_line):
    instruction_line = instruction_line.replace('^', '**')
    return eval(instruction_line)

def proceed_calculation(instruction, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for line in instruction:
            result = eval_calculation(line)
            # result = eval_trick(line)
            output_file.write(line.strip() + f" = {result:.2f}\n")

def main():
    parser = ArgumentParser(description='Kalkulator prosty')
    parser.add_argument('--input_file_path', type=str, default=r'textcalc_files\in.txt')
    parser.add_argument('--output_file_path', type=str, default=r'textcalc_files\out.txt')
    args = parser.parse_args()
    instruction = load_input(args.input_file_path)
    proceed_calculation(instruction, args.output_file_path)

if __name__ == "__main__":
    main()