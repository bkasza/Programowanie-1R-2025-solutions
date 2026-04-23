#%%
from colorpy import ciexyz, colormodels
import matplotlib.pyplot as plt
colormodels.init()

wavelengths = range(380, 751, 5)  # zakres widzialny
intensity = 1 # nie doszedłem do tego jak tutaj ładnie zmieniać natężenie, dlatego wystarczająco jest to znormalizować i ustawiać wartosć alpha na plotach
colors = []
for wl in wavelengths:
    xyz = ciexyz.xyz_from_spectrum([(wl, intensity)])
    hex_color = colormodels.irgb_string_from_xyz(xyz)
    colors.append(hex_color)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(wavelengths, intensity * len(wavelengths), color=colors, width=5)
ax.set_xlabel('Długość fali [Wavelength] (nm)')
ax.set_title('Widmo światła widziialnego')

# %%
