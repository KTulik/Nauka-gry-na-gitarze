import pyaudio
import numpy as np
import math

sample_rate = 44100  # Częstotliwość próbkowania


def play(frequency_list, chord_duration=2.0, note_duration=0.0, direction='down', amplitude=1.0):

    # sprawdzenie czy frequency_list to na pewno lista, jeżeli nie to zamienia zmienną na listę
    if not isinstance(frequency_list, list):
        frequency_list = [frequency_list]
    # Obliczanie liczby próbek na podstawie czasu trwania
    num_samples = int(sample_rate * chord_duration)

    # Tworzenie tablicy próbek dźwięku
    samples = np.zeros(num_samples, dtype=np.float32)

    # Generowanie próbek dźwięku dla każdej nuty akordu
    if (direction == 'up'):
        frequency_list.reverse()

    for index, frequency in enumerate(frequency_list):

        # Tworzenie próbek dźwięku sinusoidalnego dla danej częstotliwości
        note_samples = np.zeros(num_samples, dtype=np.float32)

        # obliczanie przeszunięcia dla danej nuty
        delta_t = int(note_duration * index / chord_duration * num_samples)

        for i in range(delta_t, num_samples):

            # Obliczanie aktualnego czasu dla próbki
            t = float(i) / sample_rate
            note_samples[i] = amplitude * \
                math.sin(2.0 * math.pi * frequency * t)

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

# def check_amplitude(frequency):

#     if frequency < 0:
#         frequency = 0
#     if frequency > 2000:
#         frequency = 2000

#     frequency_range = 2000
#     amplitude_min = 0.0
#     new_amplitude = (
#         (frequency * (-(1.0 - amplitude_min)) / frequency_range) + 1.0)
#     print(new_amplitude)
