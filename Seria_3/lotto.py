import random

def lotto_1():
    "Standardowe podejście, to wykorzystanie samplowania z random.sample, które zwraca unikalne elementy z podanego zakresu. Następnie sortujemy wynik i zwracamy jako listę."
    lotto_numbers = random.sample(range(1, 50), 6)
    lotto_numbers.sort()
    return lotto_numbers

def lotto_2():
    "Ponieważ chcemy uniknąć powtarzających się liczb, możemy użyć zbioru, który automatycznie dba o unikalność elementów. Następnie sortujemy wynik i zwracamy jako listę."
    lotto_set = set()
    while len(lotto_set) < 6:
        lotto_set.add(random.randint(1, 49))
    lotto_numbers = sorted(lotto_set)
    return lotto_numbers

if __name__ == "__main__":
    print("Lotto numbers (method 1):", lotto_1())
    print("Lotto numbers (method 2):", lotto_2())
    