from XORKeyScrambler import XORKeyScrambler
from V34Scrambler import V34Scrambler
from BLEScrambler import BLEScrambler
from DBEScrambler import DBEScrambler
from Sender import Sender
from Receiver import Receiver
from Channel import Channel
import WriteData
import random


def main():
    while True:
        scrambler = get_scrambler()
        sender = Sender(scrambler)
        receiver = Receiver(scrambler)
        channel = Channel()
        channel.receive_data(sender.send_data(generate_data()))
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
    print("4. DVB")
    print("5. Run tests")
    choice = input()
    if choice == '1':
        return XORKeyScrambler()
    elif choice == '2':
        return V34Scrambler()
    elif choice == '3':
        pass
        return BLEScrambler()
    elif choice == '4':
        return DBEScrambler()
    elif choice == '5':
        return run_test()
    else:
        print("Incorrect value, defaulting to XOR scrambler")
        return XORKeyScrambler()


def run_test():
    data = []
    to_send = generate_data()
    name = input("Name file:")
    for i in range(100):
        DBE_data = test_scrambler(DBEScrambler(), to_send)
        XOR_data = test_scrambler(XORKeyScrambler(), to_send)
        V34_data = test_scrambler(V34Scrambler(), to_send)
        data.append(str(DBE_data) + ',' + str(XOR_data) + ',' + str(V34_data))

    print(data)
    WriteData.write_data(data, name)
    pass


def test_scrambler(scrambler, to_send):
    sender = Sender(scrambler)
    receiver = Receiver(scrambler)
    channel = Channel()
    channel.receive_data(sender.send_data(to_send))
    receiver.receive_data(channel.send_data())
    return receiver.compare(sender.get_signal())


def generate_data():
    # Ask user for 0/1 amount, length
    signal_length = int(input("Enter signal length:"))
    number_of_zeros = int(input("Enter number of zeros: "))
    number_of_ones = signal_length - number_of_zeros
    signal = [1] * number_of_ones + [0] * number_of_zeros
    random.shuffle(signal)

    return signal


if __name__ == '__main__':
    main()
