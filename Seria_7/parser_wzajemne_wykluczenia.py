from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-odczyt", "--odczyt", action = "store_true")
    group.add_argument("-zapis", "--zapis", action = "store_true")
    args = parser.parse_args()
    print(args)

if __name__ == '__main__':
    main()