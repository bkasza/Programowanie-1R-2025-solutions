from argparse import ArgumentParser

def load_grocery_list(path: str):
    with open(path, 'r') as grocery_list:
        return grocery_list.readlines()

def eval_bill(grocery_list):
    value = 0
    for line in grocery_list:
        if len(line.strip()):
            cost = line.split(' ')[-1] #alternatywnie split() bez argumentów, wtedy bierzemy pod uwagę wszystkie białe znaki
            cost = float(cost)
            value += cost
    return value

def main():
    parser = ArgumentParser(description='Obliczanie kwoty do zapłaty')
    parser.add_argument("grocery_list_path", type=str)
    args = parser.parse_args()
    gl = load_grocery_list(args.grocery_list_path)
    print(f"Rachunek na kwotę {eval_bill(gl)}")

if __name__ == "__main__":
    main()