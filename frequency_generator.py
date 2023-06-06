import pyaudio
import numpy as np
import math

# Parametry symulacji dźwięku
sample_rate = 44100  # Częstotliwość próbkowania
# frequency = 440  # Częstotliwość dźwięku w Hz (tutaj przykład to dźwięk A4)


def play_note(frequency, duration=2, amplitude=1.0):

    # przeskalowanie amplitudy, aby pozoim dzwieku był podobny
    if frequency < 0:
        frequency = 0
    if frequency > 2000:
        frequency = 2000

    frequency_range = 2000
    amplitude_min = 0.45
    new_amplitude = amplitude * \
        ((frequency * (-(1.0 - amplitude_min)) / frequency_range) + 1.0)

    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku sinusoidalnego
    for i in range(num_samples):
        t = float(i) / sample_rate  # Obliczanie aktualnego czasu dla próbki
        samples[i] = new_amplitude * math.sin(2.0 * math.pi * frequency * t)

    # Inicjalizacja obiektu PyAudio
    p = pyaudio.PyAudio()

    # Otwieranie strumienia audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Odtwarzanie próbek dźwięku
    stream.write(samples.tobytes())

    # Zamykanie strumienia audio
    stream.stop_stream()
    stream.close()

    # Wyłączanie PyAudio
    p.terminate()


def check_amplitude(frequency):

    if frequency < 0:
        frequency = 0
    if frequency > 2000:
        frequency = 2000

    frequency_range = 2000
    amplitude_min = 0.0
    new_amplitude = (
        (frequency * (-(1.0 - amplitude_min)) / frequency_range) + 1.0)
    print(new_amplitude)


def play_chord(frequency_list, duration=2.0, amplitude=1.0):

    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku dla każdej nuty akordu
    for frequency in frequency_list:
        # Tworzenie próbek dźwięku sinusoidalnego dla danej częstotliwości
        note_samples = np.zeros(num_samples, dtype=np.float32)
        for i in range(num_samples):
            # Obliczanie aktualnego czasu dla próbki
            t = float(i) / sample_rate
            note_samples[i] = math.sin(2.0 * math.pi * frequency * t)

        # Dodawanie próbek dla danej nuty do ogólnych próbek akordu
        samples += note_samples

    # Normalizacja próbek do zakresu [-1, 1]
    samples /= np.max(np.abs(samples))

    # Inicjalizacja obiektu PyAudio
    p = pyaudio.PyAudio()

    # Otwieranie strumienia audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Odtwarzanie próbek dźwięku
    stream.write(samples.tobytes())

    # Zamykanie strumienia audio
    stream.stop_stream()
    stream.close()

    # Wyłączanie PyAudio
    p.terminate()


def play_chord_note_by_note(frequency_list, note_duration=0.2, chord_duration=2.0, amplitude=1.0):
    frequency_list = list(frequency_list)

    for frequency in frequency_list:
        play_note(frequency, note_duration, amplitude)

    play_chord(frequency_list, chord_duration, amplitude)


def play_sweep_chord_at_the_end(frequency_list, note_duration=0.2, chord_duration=2.0, amplitude=1.0):

    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * chord_duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku dla każdej nuty akordu
    for index, frequency in enumerate(frequency_list):
        # Tworzenie próbek dźwięku sinusoidalnego dla danej częstotliwości
        note_samples = np.zeros(num_samples, dtype=np.float32)
        for i in range(num_samples):
            # Obliczanie aktualnego czasu dla próbki
            delta_t = note_duration * index
            t = float(i) / sample_rate + delta_t
            if t > num_samples / sample_rate:
                t = num_samples / sample_rate
            note_samples[i] = math.sin(2.0 * math.pi * frequency * t)

        # Dodawanie próbek dla danej nuty do ogólnych próbek akordu
        samples += note_samples

    # Normalizacja próbek do zakresu [-1, 1]
    samples /= np.max(np.abs(samples))

    # Inicjalizacja obiektu PyAudio
    p = pyaudio.PyAudio()

    # Otwieranie strumienia audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Odtwarzanie próbek dźwięku
    stream.write(samples.tobytes())

    # Zamykanie strumienia audio
    stream.stop_stream()
    stream.close()

    # Wyłączanie PyAudio
    p.terminate()


def play_sweep_chord_at_the_end(frequency_list, note_duration=0.2, chord_duration=2.0, amplitude=1.0):

    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * chord_duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku dla każdej nuty akordu
    for index, frequency in enumerate(frequency_list):
        # Tworzenie próbek dźwięku sinusoidalnego dla danej częstotliwości
        note_samples = np.zeros(num_samples, dtype=np.float32)
        for i in range(num_samples):
            # Obliczanie aktualnego czasu dla próbki
            delta_t = note_duration * index
            t = float(i) / sample_rate + delta_t
            if t > num_samples / sample_rate:
                t = num_samples / sample_rate
            note_samples[i] = math.sin(2.0 * math.pi * frequency * t)

        # Dodawanie próbek dla danej nuty do ogólnych próbek akordu
        samples += note_samples

    # Normalizacja próbek do zakresu [-1, 1]
    samples /= np.max(np.abs(samples))

    # Inicjalizacja obiektu PyAudio
    p = pyaudio.PyAudio()

    # Otwieranie strumienia audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Odtwarzanie próbek dźwięku
    stream.write(samples.tobytes())

    # Zamykanie strumienia audio
    stream.stop_stream()
    stream.close()

    # Wyłączanie PyAudio
    p.terminate()


def play_sweep_chord(frequency_list, note_duration=0.2, chord_duration=2.0, amplitude=1.0):

    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * chord_duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku dla każdej nuty akordu
    for index, frequency in enumerate(frequency_list):
        # Tworzenie próbek dźwięku sinusoidalnego dla danej częstotliwości
        note_samples = np.zeros(num_samples, dtype=np.float32)
        delta_t = int(note_duration * index / chord_duration * num_samples)
        for i in range(delta_t, num_samples):
            # Obliczanie aktualnego czasu dla próbki
            t = float(i) / sample_rate
            note_samples[i] = math.sin(2.0 * math.pi * frequency * t)

        # Dodawanie próbek dla danej nuty do ogólnych próbek akordu
        samples += note_samples

    # Normalizacja próbek do zakresu [-1, 1]
    samples /= np.max(np.abs(samples))

    # Inicjalizacja obiektu PyAudio
    p = pyaudio.PyAudio()

    # Otwieranie strumienia audio
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # Odtwarzanie próbek dźwięku
    stream.write(samples.tobytes())

    # Zamykanie strumienia audio
    stream.stop_stream()
    stream.close()

    # Wyłączanie PyAudio
    p.terminate()
