import random

class XORKeyScrambler:
    def __init__(self):
        self.key = generate_key(256)

    def scramble(self, signal):
        scrambled_signal = ""
        k = 0
        for i in range(len(signal)):

            # XOR each bit of the signal with the corresponding bit of the key
            if signal[i] == self.key[k]:
                scrambled_signal += '0'
            else:
                scrambled_signal += '1'
            k += 1
            if k == len(self.key):
                k = 0
        return scrambled_signal

    def descramble(self,signal):
        descrambled_signal = ""
        k = 0

        for i in range(len(signal)):

            # XOR each bit of the signal with the corresponding bit of the key
            if signal[i] == self.key[k]:
                descrambled_signal += '0'
            else:
                descrambled_signal += '1'
            k += 1
            if k == len(self.key):
                k = 0
        return descrambled_signal

def generate_key(signal):
    length = signal
    binary_string = ''.join(str(random.randint(0, 1)) for _ in range(length))
    return binary_string

