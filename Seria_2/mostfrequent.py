import sys
from collections import Counter

def mostfrequent(arg):
    """Korzystamy z biblioteki collections z klasą Counter O(n)"""
    counter = Counter(arg)
    max_count = max(counter.values()) # liczba wystapien
    result = [(item, count) for item, count in counter.items() if count == max_count] # wez tylko te z maksymalna liczba wystapien
    print(result)

def mostfrequent_naive(arg):
    """Implementacja naiwna, bez uzycia Countera O(n^2)"""
    max_count = 0
    result = []
    for item in arg:
        count = arg.count(item)
        if count > max_count:
            max_count = count
            result = [(item, count)]
        elif count == max_count and (item, count) not in result:
            result.append((item, count))
    print(result)

def mostfrequent_sorted(arg):
    """Implementacja naiwna, ale sortujemy liste najpierw, zeby nie liczyc tego samego elementu wielokrotnie O(n log n) + O(n) = O(n log n)"""
    if not arg:
        print([])
        return
    
    sorted_arg = sorted(arg)
    max_count = 1
    current_count = 1
    current_item = sorted_arg[0]
    result = []
    
    for i in range(1, len(sorted_arg)):
        if sorted_arg[i] == current_item:
            current_count += 1  # Ten sam element - zwiększ licznik
        else:
            # Nowy element - zapisz poprzedni
            if current_count > max_count:
                max_count = current_count
                result = [(current_item, current_count)]
            elif current_count == max_count:
                result.append((current_item, current_count))
            
            current_item = sorted_arg[i]
            current_count = 1
    
    # Sprawdź ostatni element
    if current_count > max_count:
        result = [(current_item, current_count)]
    elif current_count == max_count:
        result.append((current_item, current_count))
    
    print(result)

if __name__ == "__main__":
    # mostfrequent(sys.argv[1:])
    mostfrequent_naive(sys.argv[1:])
    mostfrequent_sorted(sys.argv[1:])