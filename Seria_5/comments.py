from argparse import ArgumentParser


def remove_comments(marker, input_file_name, output_file_name):
    with (
        open(input_file_name, "r") as input_file,
        open(output_file_name, "w") as output_file,
    ):
        for line in input_file:
            if not line.strip().startswith(marker):
                # strip jest istotny, bo usuwamy biale znaki z poczatku linii, zeby nie bylo problemu z wcieciami
                output_file.write(line)


def main():
    parser = ArgumentParser(description="Remove comments from a file")
    parser.add_argument(
        "marker", type=str, help="Znak, który oznacza początek komentarza"
    )
    parser.add_argument(
        "input_file", type=str, help="Nazwa pliku wejściowego ze ścieżką"
    )
    parser.add_argument(
        "output_file", type=str, help="Nazwa pliku wyjściowego ze ścieżką"
    )
    args = parser.parse_args()
    remove_comments(args.marker, args.input_file, args.output_file)


if __name__ == "__main__":
    main()
