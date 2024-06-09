import random
from utils import signal_to_string

class Sender:
    def __init__(self, scrambler):
        self.data = None
        self.signal_after_scrambling = None
        self.scrambler = scrambler

    def send_signal(self):
        self.data = self.generate_signal()
        self.signal_after_scrambling = self.scrambler.scramble(self.data)
        return self.signal_after_scrambling

    # metoda do testow
    def send_data(self):
        self.signal_after_scrambling = self.scrambler.scramble(self.data)
        return self.signal_after_scrambling

    # metoda do menu
    def print_data(self):
        print("Sender:")
        print("Generated signal: " + signal_to_string(self.data))
        print("Signal after scrambling: " + signal_to_string(self.signal_after_scrambling))
        print()

    def get_signal(self):
        return self.data
    '''
    def generate_data(self):
        #Ask user for 0/1 amount, length
        signal_length = int(input("Enter signal length:"))
        number_of_zeros = int(input("Enter number of zeros: "))
        number_of_ones = signal_length - number_of_zeros
        signal = [1] * number_of_ones + [0] * number_of_zeros
        random.shuffle(signal)
        return signal
    '''
    # metoda do testow
    def generate_data(self, signal_length, percentage_ones):
        number_of_ones = int(signal_length * percentage_ones / 100)
        number_of_zeros = signal_length - number_of_ones
        signal = [1] * number_of_ones + [0] * number_of_zeros
        random.shuffle(signal)
        return signal
        
    # metoda do testow metoda do menu
    def generate_signal(self):
        # Ask user for 0/1 amount, length
        signal_length = int(input("Enter signal length:"))
        number_of_zeros = int(input("Enter number of zeros: "))
        number_of_ones = signal_length - number_of_zeros
        signal = [1] * number_of_ones + [0] * number_of_zeros
        random.shuffle(signal)
        return signal
