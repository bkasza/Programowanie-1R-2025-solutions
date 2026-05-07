"Pobawmy się w psucie kodu"

# %%
lista = [1, 2, 3]

slownik = {"a": 1, "b": 2}

# %%
try:
    print(lista[10])
except IndexError as e:
    print(f"Nie można dostać się do elementu o indeksie 10: {e}")
finally:
    print("To się wykona zawsze, niezaleznie od tego czy wyjątek był")
#%%
try:
    print(slownik["c"])
except KeyError as e:
    print(f"Nie można dostać się do klucza: {e}")

# %%
