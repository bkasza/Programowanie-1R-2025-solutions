import sys
from collections import Counter

# Na końcu chcemy mieć posortowane 
def words(arg):
    counter = Counter(arg)
    sorted_counter = {key: value for key, value in sorted(counter.items())}
    print(sorted_counter)

if __name__ == "__main__":
    words(sys.argv[1:])