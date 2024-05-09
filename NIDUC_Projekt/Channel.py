import random

class Channel:
    def __init__(self,sender,receiver):
        self.key = None
        self.noise_signal = None
        self.signal_after_scrambling = None
    def receive(self,signal):
        self.signal_after_scrambling = signal.split(',')[0]
        self.key = signal.split(',')[1]
    def send(self):
        error_chance = calculate_error(self.signal_after_scrambling)
        error_chance_key= calculate_error(self.key)
        self.noise_signal = generate_noise(self.signal_after_scrambling, error_chance) + ',' + generate_noise(self.key, error_chance_key)
        return self.noise_signal

    def print_data(self):
        print("Channel:")
        print("Scrambled with error, key with error: ", self.noise_signal)

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