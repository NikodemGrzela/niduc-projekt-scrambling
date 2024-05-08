import random


def calculate_error(signal):
    zeros_count = 0
    max_zeros_count = 0
    for bit in signal:
        if bit == '0':
            zeros_count += 1
        else:
            zeros_count = 0
        max_zeros_count = max(max_zeros_count, zeros_count)
    return max_zeros_count / len(signal)


def generate_noise(signal, error_chance):
    noisy_signal = ""
    for bit in signal:
        noisy_signal += bit if random.random() > error_chance else ('1' if bit == '0' else '0')
    return noisy_signal


class Channel:
    def __init__(self):
        self.key = None
        self.noise_signal = None
        self.signal_after_scrambling = None

    def receive(self, signal):
        self.signal_after_scrambling = signal.split(',')[0]
        self.key = signal.split(',')[1]

    def send(self):
        error_chance = calculate_error(self.signal_after_scrambling)
        self.noise_signal = (generate_noise(self.signal_after_scrambling, error_chance)
                             + ',' + generate_noise(self.key, error_chance))
        return self.noise_signal

    def print_data(self):
        print("Channel:")
        print("Scrambled with error, key with error: ", self.noise_signal)
        error_chance = int(calculate_error(self.signal_after_scrambling) * 100)
        print(f"Error chance was: {error_chance}%")
