import pyaudio
import numpy as np
import math

sample_rate = 44100  # Frequency of samples


def play(frequency_list, chord_duration=2.0, note_duration=0.0, direction='down', amplitude=1.0):

    # check if frequency_list is list
    if not isinstance(frequency_list, list):
        frequency_list = [frequency_list]
    # calculate number of samples
    num_samples = int(sample_rate * chord_duration)

    # make array of sound sample
    samples = np.zeros(num_samples, dtype=np.float32)

    # direction of chord
    if (direction == 'up'):
        frequency_list.reverse()

    for index, frequency in enumerate(frequency_list):

        # make sinusoidal wave
        note_samples = np.zeros(num_samples, dtype=np.float32)

        # calculate delta for separate notes
        delta_t = int(note_duration * index / chord_duration * num_samples)

        for i in range(delta_t, num_samples):

            # calculate actual sample time
            t = float(i) / sample_rate
            note_samples[i] = amplitude * \
                math.sin(2.0 * math.pi * frequency * t)

        # add separate note samples 
        samples += note_samples

    # Normalize amplitude of sinusoidal wave
    samples /= np.max(np.abs(samples))

    # Initialize PyAudio object
    p = pyaudio.PyAudio()

    # Open audio stream
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    # play wave
    stream.write(samples.tobytes())

    # close audio stream
    stream.stop_stream()
    stream.close()

    # turn off PyAudio
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
