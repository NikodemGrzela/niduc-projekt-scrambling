import random
from utils import signal_to_string

class Receiver:
    def __init__(self, descrambler):
        self.signal = None
        self.signal_after_descrambling = None
        self.descrambler = descrambler

    def receive_data(self, signal):
        self.signal = signal
        self.signal_after_descrambling = self.descrambler.descramble(signal)

    def print_data(self):
        print("Receiver:")
        print("Received signal: " + signal_to_string(self.signal))
        print("Signal after descrambling: " + signal_to_string(self.signal_after_descrambling))
        print()

    def compare(self, signal2):
        equal = 0
        for i in range(len(self.signal_after_descrambling)):
            if self.signal_after_descrambling[i] == signal2[i]:
                equal = equal + 1
        print(equal / len(self.signal_after_descrambling) * 100)
        return equal / len(self.signal_after_descrambling) * 100

