"""Podana implementacja pokazuje ciut inną filozofię, gdzie starałem się przestawić dane w taki sposób, by dało się wygodnie odczytywać szukane statystyki.
Jest to filozofia bliższa używania arkuszy, tudzież bibliotek takich ja pandas. Niemniej nie jest to najbardziej eleganckie, dlatego standardowe rozwiązanie jest w ludnosc_siplify."""
import json
import matplotlib.pyplot as plt
# %%

stat_keys = ["ludność", "powierzchnia km2", "gęstość zaludnienia"]


# %%
def load_data():
    with open(r"Seria_3\ludnosc.json", "r") as plik:
        dane = json.load(plik)
    return dane


def ask_wojewodztwo():
    print("Podaj województwo (lub Polska):")
    return input()


def ask_statystyka():
    print("Podaj statystykę (ludność, powierzchnia km2, gęstość):")
    stat = input()

    if stat == "gęstość":
        stat = "gęstość zaludnienia"

    return stat


# %%
def process_data(data):
    """
    zmieniamy format:
    rok -> województwo -> statystyka
    na
    województwo -> statystyka -> rok
    """
    processed_data = {}
    polska_data = {"ludność": {}, "powierzchnia km2": {}, "gęstość zaludnienia": {}}
    for rok, wojewodztwa in data.items():
        for woj, statystyki in wojewodztwa.items():
            if woj not in processed_data:
                processed_data[woj] = {key: {} for key in stat_keys}

            lud = statystyki["ludność"]
            pow_km = statystyki["powierzchnia km2"]

            processed_data[woj]["ludność"][rok] = lud
            processed_data[woj]["powierzchnia km2"][rok] = pow_km
            processed_data[woj]["gęstość zaludnienia"][rok] = lud / pow_km

            # sumowanie dla Polski
            if rok not in polska_data["ludność"]:
                polska_data["ludność"][rok] = 0
                polska_data["powierzchnia km2"][rok] = 0

            polska_data["ludność"][rok] += lud
            polska_data["powierzchnia km2"][rok] += pow_km
    # obliczamy gęstość dla Polski
    for rok in polska_data["ludność"]:
        polska_data["gęstość zaludnienia"][rok] = (
            polska_data["ludność"][rok] / polska_data["powierzchnia km2"][rok]
        )
    processed_data["Polska"] = polska_data
    return processed_data


# %%
def plot_data(processed_data, woj, stat):
    if woj not in processed_data:
        print("Nie ma takiego województwa.")
        return
    if stat not in processed_data[woj]:
        print("Nie ma takiej statystyki.")
        return
    years = sorted(processed_data[woj][stat].keys())
    values = [processed_data[woj][stat][y] for y in years]
    plt.plot(years, values)
    plt.xlabel("Rok")
    plt.ylabel(stat)
    plt.title(f"{stat} w {woj} na przestrzeni lat")
    plt.show()

    # %%
data = load_data()
processed_data = process_data(data)

woj = ask_wojewodztwo()
stat = ask_statystyka()

plot_data(processed_data, woj, stat)
# %%
