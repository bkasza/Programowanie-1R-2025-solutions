"rozne metody sprawdzania palindromow, odsiew znakow specjalnych, redukcja do pojedynczych liter"
import re
import sys
from typing import Union
import string

def check_palindrome_with_re(wyrazenie: Union[str, list]):
    "metoda z wykorzystaniem regexa do odsiewu znakow specjalnych"
    if isinstance(wyrazenie, list):
        wyrazenie = "".join(wyrazenie)
    wyrazenie = re.sub(r'[^a-zA-Z]', '', wyrazenie).lower()
    
    return wyrazenie == wyrazenie[::-1]

def check_palindrome_with_string(wyrazenie: Union[str, list]):
    "prosta metoda z wykorzystaniem stringa, bez regexa, ale z list comprehension"
    if isinstance(wyrazenie, list):
        wyrazenie = "".join(wyrazenie)
    wyrazenie = "".join([char for char in wyrazenie if char in string.ascii_letters]).lower()
    
    return wyrazenie == wyrazenie[::-1]

def check_palindrome_with_filter(wyrazenie: str | list):
    "najbardziej pythonowe, z wykorzystaniem filtera i funkcji isalpha"
    if isinstance(wyrazenie, list):
        wyrazenie = "".join(wyrazenie)
    wyrazenie = "".join(filter(str.isalpha, wyrazenie)).lower()
    
    return wyrazenie == wyrazenie[::-1]

def palindrome_two_pointers(wyrazenie: Union[str, list]):
    "wydajne pamieciowo, bez tworzenia nowych stringow, ale z dwoma wskaznikami"
    left = 0
    right = len(wyrazenie) - 1

    while left < right:
        while left < right and not wyrazenie[left].isalpha():
            left += 1
        while left < right and not wyrazenie[right].isalpha():
            right -= 1
        if wyrazenie[left].lower() != wyrazenie[right].lower():
            return False
        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    args = sys.argv[1:]
    for wyrazenie in args:
        if check_palindrome_with_re(wyrazenie):
            print(f"regex - podane wyrazenie jest palindromem {wyrazenie}")
        if check_palindrome_with_string(wyrazenie):
            print(f"string - podane wyrazenie jest palindromem {wyrazenie}")
        if check_palindrome_with_filter(wyrazenie):
            print(f"filter - podane wyrazenie jest palindromem {wyrazenie}")
        if palindrome_two_pointers(wyrazenie):
            print(f"two pointers - podane wyrazenie jest palindromem {wyrazenie}")