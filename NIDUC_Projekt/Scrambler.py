import random


def generate_key(signal):
    return ''.join(random.choice('01') for _ in range(len(signal)))


class Scrambler:
    def __init__(self):
        self.key = None
        self.signal = None

    def scramble(self, signal, key=None):
        self.signal = signal
        self.key = key if key is not None else generate_key(signal)
        return self.xor_scramble() + ',' + self.key

    def xor_scramble(self):
        scrambled_signal = ""
        for i in range(len(self.signal)):
            scrambled_signal += str(int(self.signal[i]) ^ int(self.key[i % len(self.key)]))
        return scrambled_signal

    '''
    OLD SCRAMBLE
        def xor_scramble(self):
            scrambled_signal = ""
            k = 0
            for i in range(len(self.signal)):
                scrambled_signal += '1' if self.signal[i] != self.key[k] else '0'
                k = (k + 1) % len(self.key)
            return scrambled_signal
    '''
