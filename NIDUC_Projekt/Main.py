from XORKeyScrambler import XORKeyScrambler
from V34Scrambler import V34Scrambler
from BLEScrambler import BLEScrambler
from Sender import Sender
from Receiver import Receiver
from Channel import Channel


def main():
    while True:
        scrambler = get_scrambler()
        sender = Sender(scrambler)
        receiver = Receiver(scrambler)
        channel = Channel()
        channel.receive_data(sender.send_data())
        receiver.receive_data(channel.send_data())

        print("=========================")
        sender.print_data()
        scrambler.print_data()
        channel.print_data()
        receiver.print_data()

        receiver.compare(sender.get_signal())
        print("=========================")

def get_scrambler():
    print("Provide scrambler type:")
    print("1. XOR with key")
    print("2. V.34")
    print("3. BLE")
    choice = input()
    if choice == '1':
        return XORKeyScrambler()
    elif choice == '2':
        return V34Scrambler()
    elif choice =='3':
        return BLEScrambler()
    else:
        print("Incorrect value, defaulting to XOR scrambler")
        return XORKeyScrambler()

if __name__ == '__main__':
    main()

