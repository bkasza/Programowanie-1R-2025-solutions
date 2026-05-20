"najwazniejsze, co musicie umiec z numpy to fourier tak naprawdę"

#%%
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100, endpoint=False)

y1 = np.sin(2 * np.pi * 5 * t)  # 5 Hz
y2 = 0.5 * np.cos(2 * np.pi * 10 * t)  # 10 Hz
y3 = 0.25 * np.sin(2 * np.pi * 15 * t)  # 15 Hz

signal = y1 + y2 + y3

plt.plot(t, signal)
# %%
fft_result = np.fft.fft(signal)
print(type(fft_result), fft_result.shape, type(fft_result[0]), fft_result[0])
#%%
# %%

fft_freqs = np.fft.fftfreq(len(signal), d=t[1] - t[0])
plt.scatter(fft_freqs, np.abs(fft_result))
plt.xlim(-20, 20)
plt.ylabel("amplituda")
plt.xlabel("czestosc [Hz]")
plt.title("Widmo sygnału")
#%%
print(fft_freqs[np.argsort(np.abs(fft_result))[-6:]])
# %%
"odsyzskanie przebiegu czasowego"

recovered_signal = np.fft.ifft(fft_result)
plt.plot(t, recovered_signal.real)
# %%
