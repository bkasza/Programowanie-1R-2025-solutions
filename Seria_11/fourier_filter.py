import numpy as np
from argparse import ArgumentParser
import matplotlib.pyplot as plt
from sympy import plot



def fourier_filter(signal: np.ndarray, cutoff_freq: float, sampling_rate: float) -> np.ndarray:
    """
    Aplikuje dolnoprzepustowy filtr Fouriera do wejściowego sygnału.

    Parametry:
    signal (np.ndarray): Sygnał wejściowy do przefiltrowania.
    cutoff_freq (float): Częstotliwość odcięcia dla filtru dolnoprzepustowego w Hz.
    sampling_rate (float): Częstotliwość próbkowania sygnału w Hz.

    Zwraca:
    np.ndarray: Przefiltrowany sygnał.
    """
    num_samples = len(signal)
    fourier_transform = np.fft.fft(signal)
    freqs = np.fft.fftfreq(num_samples, d=1/sampling_rate)
    mask = np.abs(freqs) > cutoff_freq
    fourier_transform[mask] = 0
    filtered_signal = np.fft.ifft(fourier_transform)

    return np.real(filtered_signal)

def better_fourier_filter(signal: np.ndarray, cutoff_freq: float, sampling_rate: float) -> np.ndarray:
    """
    Aplikuje filtr Fouriera z supergaussowskim oknem do wejściowego sygnału.
    
    Parametry:
    signal (np.ndarray): Sygnał wejściowy do przefiltrowania.
    cutoff_freq (float): Częstotliwość odcięcia dla filtru w Hz.
    sampling_rate (float): Częstotliwość próbkowania sygnału w Hz.

    Zwraca:
    np.ndarray: Przefiltrowany sygnał.
    """

    num_samples = len(signal)
    fourier_transform = np.fft.fft(signal)
    freqs = np.fft.fftfreq(num_samples, d=1/sampling_rate)
    super_gaussian_window = np.exp(-0.5 * (freqs / cutoff_freq)**4)
    filtered_fourier = fourier_transform * super_gaussian_window
    filtered_signal = np.fft.ifft(filtered_fourier)

    return np.real(filtered_signal)

def signal_generator(signal_fun: str,sampling_rate: float, duration: float) -> np.ndarray:
    """
    Generuje sygnał w postaci ewaluacji podanego stringa.
    Parametry:
    signal_fun (str): Funkcja do wykonania.
    sampling_rate (float): Częstotliwość próbkowania w Hz.
    duration (float): Czas trwania sygnału w sekundach.

    Zwraca:
    np.ndarray: Wygenerowany sygnał.
    """
    t = np.arange(0, duration, 1/sampling_rate)
    x = t # na wypadek jakby ktos podał t
    signal = eval(signal_fun) 
    return signal

def noise_generator(signal: np.ndarray, noise_level: float) -> np.ndarray:
    """
    Dodaje szum gaussowski do sygnału wejściowego.

    Parametry:
    signal (np.ndarray): Sygnał wejściowy, do którego dodany zostanie szum.
    noise_level (float): Odchylenie standardowe szumu gaussowskiego.

    Zwraca:
    np.ndarray: Zaszumiony sygnał.
    """
    noise = np.random.normal(0, noise_level, size=signal.shape)
    return signal + noise

def plot_signals(original_signal: np.ndarray, noisy_signal: np.ndarray, filtered_signal: np.ndarray, sg_filtered_signal: np.ndarray, sampling_rate: float):
    """
    Rysuje sygnał oryginalny, zaszumiony i przefiltrowany.

    Parametry:
    original_signal (np.ndarray): Oryginalny, czysty sygnał.
    noisy_signal (np.ndarray): Sygnał z dodanym szumem.
    filtered_signal (np.ndarray): Sygnał po zastosowaniu filtru Fouriera.
    sampling_rate (float): Częstotliwość próbkowania sygnałów w Hz.
    """

    time = np.arange(len(original_signal)) / sampling_rate

    plt.figure(figsize=(12, 8))
    plt.subplot(4, 1, 1)
    plt.title("sygnał oryginalny")
    plt.plot(time, original_signal)
    plt.xlabel("t [s]")

    plt.subplot(4, 1, 2)
    plt.title("zaszumiony sygnał")
    plt.plot(time, noisy_signal)
    plt.xlabel("t")

    plt.subplot(4, 1, 3)
    plt.title("odfiltrowany sygnał")
    plt.plot(time, filtered_signal)
    plt.xlabel("t [s]")

    plt.subplot(4, 1, 4)
    plt.title("odfiltrowany sygnał z supergaussowskim oknem")
    plt.plot(time, sg_filtered_signal)
    plt.xlabel("t [s]")

    plt.tight_layout()
    # plt.savefig(r"fourier_plots\fourier_filter.png")
    plt.show()

def main():
    parser = ArgumentParser(description="Przykład zastosowania filtru Fourierowskiego do sygnału")
    # parser.add_argument("--signal_fun", type=str, default="np.sin(t) + 0.5 * np.cos(2 * t) + 0.25 * np.sin(3 * t)", help="funkcja sygnału w postaci stringa kodu z wykorzystaniem numpy")
    parser.add_argument("--signal_fun", type=str, default="np.exp(-(t-5)**2/0.5)", help="funkcja sygnału w postaci stringa kodu z wykorzystaniem numpy")
    parser.add_argument("--sampling_rate", type=float, default=100.0, help="probkowanie sygnału w Hz")
    parser.add_argument("--duration", type=float, default=10.0, help="czas trwania sygnału w sekundach")
    parser.add_argument("--cutoff_freq", type=float, default=0.55, help="czestosc odciecia filtru w Hz")
    parser.add_argument("--noise_level", type=float, default=0.1, help="sigma gaussowskiego szumu")
    args = parser.parse_args()
    signal = signal_generator(args.signal_fun, args.sampling_rate, args.duration)
    noisy_signal = noise_generator(signal, args.noise_level)
    filtered_signal = fourier_filter(noisy_signal, args.cutoff_freq, args.sampling_rate)
    better_filtered_signal = better_fourier_filter(noisy_signal, args.cutoff_freq, args.sampling_rate)
    plot_signals(signal, noisy_signal, filtered_signal, better_filtered_signal, args.sampling_rate)

if __name__ == "__main__":
    main()