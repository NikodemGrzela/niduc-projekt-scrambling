import random

from Scrambler import Scrambler


class Receiver:
    def __init__(self):
        self.signal_after_descrambling = None
        self.received = None

    def receive_data(self, signal):
        self.received = signal

        # Scramble data
        scrambler = Scrambler()
        self.signal_after_descrambling = scrambler.scramble(self.received)

    def print_data(self):
        print("Receiver:")
        print("Descrambled: ", self.signal_after_descrambling)



