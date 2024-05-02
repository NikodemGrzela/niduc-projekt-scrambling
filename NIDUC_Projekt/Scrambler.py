class Scrambler:
    def __init__(self):
        pass
    def scramble(self,signal):
        return choose(signal)


def xor_scramble(signal):
    key = input("Enter key: ")
    scrambled_signal = ""
    k=0
    for i in range(len(signal)):

        # XOR each bit of the signal with the corresponding bit of the key
        if signal[i] == key[k]:
            scrambled_signal += '0'
        else:
            scrambled_signal += '1'
        k+=1
        if k==len(key):
            k=0
    return scrambled_signal

def show_menu():
    print("1. XOR with key")

def choose(signal):
    choice = 1
    while choice != 0:
        show_menu()
        choice = input()
        if choice.isnumeric():
            choice = int(choice)

        if choice == 1:
            return xor_scramble(signal)
        else:
            print("No such an option")
