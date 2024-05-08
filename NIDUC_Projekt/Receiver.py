from Scrambler import Scrambler


class Receiver:
    def __init__(self):
        self.key = None
        self.signal_after_descrambling = None
        self.received = None

    def receive_data(self, signal):
        self.received = signal.split(',')[0]
        self.key = signal.split(',')[1]

        scrambler = Scrambler()
        scrambler.signal = self.received
        scrambler.key = self.key
        self.signal_after_descrambling = scrambler.xor_scramble()

    def print_data(self):
        print("Receiver:")
        print("Descrambled: ", self.signal_after_descrambling, " Received key: ", self.key)
