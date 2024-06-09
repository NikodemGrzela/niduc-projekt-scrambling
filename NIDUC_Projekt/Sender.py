import random
from utils import signal_to_string

class Sender:
    def __init__(self, scrambler):
        self.data = None
        self.signal_after_scrambling = None
        self.scrambler = scrambler

    def send_data(self):
        # Ask user for 0/1 amount, length
        signal_length = int(input("Enter signal length:"))
        percentage_ones = int(input("Enter percentage of ones: "))
        self.data = self.generate_data(signal_length, percentage_ones)
        self.signal_after_scrambling = self.scrambler.scramble(self.data)
        return self.signal_after_scrambling

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
    
    def generate_data(self, signal_length, percentage_ones):
        number_of_ones = int(signal_length * percentage_ones / 100)
        number_of_zeros = signal_length - number_of_ones
        signal = [1] * number_of_ones + [0] * number_of_zeros
        random.shuffle(signal)
        return signal
