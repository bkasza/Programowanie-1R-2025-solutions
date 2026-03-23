"""
słów kilka o zbiorach
plik jest w formacie python-interactive, by takowy odpalić należy mieć srodowisko przystosowane do jupytera oraz ipykernel
"""
#%%
zbior = set()

# %%
zbior.add('abc')
zbior
#%%
zbior.clear()
zbior

# %%
zbior = set(range(5))
zbior
# %%
zbior_drugi = set(range(3))
zbior | zbior_drugi #operacja sumy zbiorów A v B
# %%
zbior & zbior_drugi #operacja iloczynu zbiorów A ^ B
# %%
zbior.difference(zbior_drugi)
# %%
