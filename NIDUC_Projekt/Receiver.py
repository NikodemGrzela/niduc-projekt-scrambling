import random

from Scrambler import Scrambler


class Receiver:
    def __init__(self):
        pass

    def receive_data(self, signal):
        self.signal = signal.split(',')[0]
        self.signal_scrambled = signal.split(',')[1]
        self.received = signal.split(',')[2]

        # Scramble data
        scrambler = Scrambler()
        self.signal_after_scrambling = scrambler.scramble(self.received)

    def print_data(self):
        print("Receiver:")
        print(" generated: ", self.signal,
              " generated,scrambled" , self.signal_scrambled ,
              " with noise:", self.received,
              " descrambled: ", self.signal_after_scrambling)



