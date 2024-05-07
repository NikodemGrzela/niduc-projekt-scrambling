import random


class Scrambler:
    def __init__(self):
        self.key = None
        self.signal = None

    def scramble(self, signal):
        self.signal = signal
        self.key = generate_key(256)
        return self.choose() + ',' + self.key

    def choose(self):
        choice = 1
        while choice != 0:
            show_menu()
            choice = input()
            if choice.isnumeric():
                choice = int(choice)

            if choice == 1:
                return self.xor_scramble()
            else:
                print("No such an option")

    def xor_scramble(self):
        scrambled_signal = ""
        k = 0
        for i in range(len(self.signal)):

            # XOR each bit of the signal with the corresponding bit of the key
            if self.signal[i] == self.key[k]:
                scrambled_signal += '0'
            else:
                scrambled_signal += '1'
            k += 1
            if k == len(self.key):
                k = 0
        return scrambled_signal

    def xor_descramble(self,signal,key):
        descrambled_signal = ""
        k = 0
        print(len(signal))
        for i in range(len(signal)):

            # XOR each bit of the signal with the corresponding bit of the key
            if signal[i] == key[k]:
                descrambled_signal += '0'
            else:
                descrambled_signal += '1'
            k += 1
            if k == len(key):
                k = 0
        return descrambled_signal





def show_menu():
    print("1. XOR with key")





def generate_key(signal):
    length = signal
    binary_string = ''.join(str(random.randint(0, 1)) for _ in range(length))
    return binary_string

