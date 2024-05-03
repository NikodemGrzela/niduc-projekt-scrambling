import random
from Scrambler import Scrambler


class Sender:
    def __init__(self):
        self.data = None
        self.signal_after_scrambling = None

    def send_data(self):
        scrambler = Scrambler()
        self.data = generate_data()
        self.signal_after_scrambling = scrambler.scramble(self.data)
        return self.signal_after_scrambling

    def print_data(self):
        print("Sender:")
        print("generated: ", self.data, " after scrambling ", self.signal_after_scrambling)


def generate_data():
    #Ask user for 0/1 amount, length
    signal_length = int(input("Enter signal length:"))
    number_of_zeros = int(input("Enter number of zeros: "))
    number_of_ones = signal_length - number_of_zeros
    signal = number_of_ones * '1' + (number_of_zeros * '0')
    return scramble_string(signal)


def scramble_string(signal):
    char_list = list(signal)
    random.shuffle(char_list)
    scrambled_string = ''.join(char_list)
    return scrambled_string
