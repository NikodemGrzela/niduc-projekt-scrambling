import random
from Scrambler import Scrambler


def scramble_string(signal):
    char_list = list(signal)
    random.shuffle(char_list)
    return ''.join(char_list)


def generate_data(signal_length, number_of_zeros):
    number_of_ones = signal_length - number_of_zeros
    signal = number_of_ones * '1' + number_of_zeros * '0'
    return scramble_string(signal)


class Sender:
    def __init__(self):
        self.data = None
        self.signal_after_scrambling = None

    def send_data(self, signal_length, number_of_zeros):
        scrambler = Scrambler()
        self.data = generate_data(signal_length, number_of_zeros)
        self.signal_after_scrambling = scrambler.scramble(self.data)
        return self.signal_after_scrambling

    def print_data(self):
        print("Sender:")
        print("Generated: ", self.data, " After scrambling, key: ", self.signal_after_scrambling)
