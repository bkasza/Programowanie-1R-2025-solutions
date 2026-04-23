class Test:
    def __init__(self):
        self.text = "Hello world"

    def __str__(self):
        return self.text

    def __repr__(self) -> str:
        return "repr text"


def main():
    t = Test()
    print(repr(t))

if __name__ == "__main__":
    main()
