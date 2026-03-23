"""
pare słow o slownikach i hashowaniu
plik jest w formacie python-interactive, by takowy odpalić należy mieć srodowisko przystosowane do jupytera oraz ipykernel
"""

#%%
# słownik to zbiór par klucz-wartość, gdzie klucze są unikalne
slownik = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
slownik = dict(a='apple', b='banana', c='cherry')  # inny sposób tworzenia słownika
#%%
# słowniki są mutowalne, można je modyfikować
slownik['d'] = 'date'  # dodawanie nowej pary klucz-wartość
slownik['a'] = 'avocado'  # modyfikowanie istniejącej wartości
print(slownik)
# %%
# klucze w słowniku muszą być hashowalne, czyli niemutowalne (np. liczby, stringi, tuple)
# przykłady jak sprawdzić, czy obiekt jest hashowalny
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False
    
test_lista = [1, "hello", (1, 2), [3, 4], [[]], set([1, 2]), frozenset([1, 2]), {"key": "value"}] 
for obj in test_lista:
    print(f"{obj} is hashable: {is_hashable(obj)}")

#%%
# jezeli obiekt jest hashowalny, to istnieje jego hash, który jest liczbą całkowitą reprezentującą ten obiekt
for k in slownik.keys():
    print(f"Hash klucza '{k}': {hash(k)}")
# %%
#najwazniejsze, to umiejetnosc przechodzenia po slowniku

print(slownik.values())
print(slownik.items())
print(slownik.keys())
#%%
#mozna rowniez robic dict comprehension, czyli tworzyc slownik na podstawie innej kolekcji
lista = ['apple', 'banana', 'cherry']
slownik_owocow = {s: (s[0], s[-1]) for s in lista}  # tworzy slownik, gdzie kluczem jest owoc, a wartoscia jego pierwsza i ostatnia litera
slownik_owocow
# %%
