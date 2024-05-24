import random
from utils import signal_to_string

class Sender:
    def __init__(self, scrambler):
        self.data = None
        self.signal_after_scrambling = None
        self.scrambler = scrambler

    def send_data(self,data):
        self.data = data
        self.signal_after_scrambling = self.scrambler.scramble(self.data)
        return self.signal_after_scrambling


    def print_data(self):
        print("Sender:")
        print("Generated signal: " + signal_to_string(self.data))
        print("Signal after scrambling: " + signal_to_string(self.signal_after_scrambling))
        print()

    def get_signal(self):
        return self.data


