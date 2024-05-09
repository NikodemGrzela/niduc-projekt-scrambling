import random

from Scrambler import Scrambler


class Receiver:
    def __init__(self):
        self.key = None
        self.signal_after_descrambling = None
        self.received = None

    def receive_data(self, signal):
        self.received = signal.split(',')[0]
        self.key = signal.split(',')[1]

        # Scramble data
        scrambler = Scrambler()
        self.signal_after_descrambling = scrambler.xor_descramble(self.received,self.key)

    def print_data(self):
        print("Receiver:")
        print("Descrambled: ", self.signal_after_descrambling, " Received key: ", self.key)

    def compare(self, signal2):
        equal = 0
        for i in range(len(self.signal_after_descrambling)):
            if self.signal_after_descrambling[i] == signal2[i]:
                equal = equal + 1
        print(equal / len(self.signal_after_descrambling) * 100)
