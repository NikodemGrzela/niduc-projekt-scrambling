import random

from Scrambler import Scrambler


class Receiver:
    def __init__(self):
        pass

    def receive_data(self, signal):
        self.signal = signal

        # calculateError
        error_chance = calculate_error(signal)
        self.noise_signal = generate_noise(signal, error_chance)

        # Scramble data
        scrambler = Scrambler()
        self.signal_after_scrambling = scrambler.scramble(signal)

    def print_data(self):
        print("received: ",
              self.signal, " with noise:", self.noise_signal, " scrambled: ", self.signal_after_scrambling)


def calculate_error(signal):
    zeros_count = 0
    max_zeros_count = 0

    # count zeros
    for bit in signal:
        if bit == '0':
            zeros_count += 1
            max_zeros_count = max(max_zeros_count, zeros_count)
        else:
            zeros_count = 0

    probability = (max_zeros_count / len(signal))
    return probability


def generate_noise(signal, error_chance):
    noisy_signal = ""
    print(error_chance)
    for bit in signal:
        if random.random() < error_chance:
            if bit == '0':
                noisy_signal += '1'
            else:
                noisy_signal += '0'
        else:
            noisy_signal += bit
    return noisy_signal
