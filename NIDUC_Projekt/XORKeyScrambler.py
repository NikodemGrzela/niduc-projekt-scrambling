import random
from utils import signal_to_string

class XORKeyScrambler:
    def __init__(self):
        self.key = self.generate_key(256)

    def scramble(self, signal):
        scrambled_signal = []
        k = 0
        for i in range(len(signal)):
            # XOR each bit of the signal with the corresponding bit of the key
            if signal[i] == self.key[k]:
                scrambled_signal.append(0)
            else:
                scrambled_signal.append(1)
            k += 1
            if k == len(self.key):
                k = 0
        return scrambled_signal

    def descramble(self, signal):
        descrambled_signal = []
        k = 0

        for i in range(len(signal)):

            # XOR each bit of the signal with the corresponding bit of the key
            if signal[i] == self.key[k]:
                descrambled_signal.append(0)
            else:
                descrambled_signal.append(1)
            k += 1
            if k == len(self.key):
                k = 0
        return descrambled_signal
    
    def print_data(self):
        print("XOR Scrambler:")
        print("Key: " + signal_to_string(self.key))
        print()

    def generate_key(self, signal):
        length = signal
        key = [random.randint(0, 1) for _ in range(length)]
        return key

