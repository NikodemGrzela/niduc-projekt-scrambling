import random
from utils import signal_to_string

class Channel:
    def __init__(self):
        self.noise_signal = None
        self.signal_after_scrambling = None

    def receive_data(self,signal):
        self.signal_after_scrambling = signal

    def send_data(self):
        error_chance = calculate_error(self.signal_after_scrambling)
        self.noise_signal = generate_noise(self.signal_after_scrambling, error_chance)
        return self.noise_signal

    def print_data(self):
        print("Channel:")
        print("Signal with introduced error: " + signal_to_string(self.noise_signal))
        print()

def calculate_error(signal):
    zeros_count = 0
    max_zeros_count = 0

    # count zeros
    for bit in signal:
        if bit == 0:
            zeros_count += 1
            max_zeros_count = max(max_zeros_count, zeros_count)
        else:
            zeros_count = 0

    probability = (max_zeros_count / len(signal))
    return probability


def generate_noise(signal, error_chance):
    noisy_signal = []
    for bit in signal:
        if random.random() < error_chance:
            if bit == 0:
                noisy_signal.append(1)
            else:
                noisy_signal.append(0)
        else:
            noisy_signal.append(bit)
    return noisy_signal