
import json
import os
import matplotlib.pyplot as plt

def load_data():
    with open("ludnosc.json") as f:
        data = json.load(f)
    return data

def ask_user():
    woj = input("Podaj województwo (lub Polska): ")
    stat = input("Podaj statystykę (ludność, powierzchnia km2, gęstość zaludnienia): ")
    return woj, stat

def calculate_stat(data, woj, stat):
    years = []
    values = []
    for rok in sorted(data.keys()):
        years.append(int(rok))
        if woj == "Polska":
            lud = sum(w["ludność"] for w in data[rok].values())
            pow_km = sum(w["powierzchnia km2"] for w in data[rok].values())
        else:
            lud = data[rok][woj]["ludność"]
            pow_km = data[rok][woj]["powierzchnia km2"]
        if stat == "ludność":
            values.append(lud)
        elif stat == "powierzchnia km2":
            values.append(pow_km)
        elif stat == "gęstość zaludnienia":
            values.append(lud / pow_km)
    return years, values


def plot_stat(woj, stat, years, values):
    plt.plot(years, values)
    plt.xlabel("Rok")
    plt.ylabel(stat)
    plt.title(f"{stat} w {woj}")
    os.makedirs("ludnosc_plots", exist_ok=True)
    plt.savefig(f"ludnosc_plots/{woj}_{stat}.png")  # FIXED: Changed backslash to forward slash
    plt.show()    

def main():
    data = load_data()
    woj, stat = ask_user()
    years, values = calculate_stat(data, woj, stat)
    plot_stat(woj, stat, years, values)

if __name__ == "__main__":
    main()