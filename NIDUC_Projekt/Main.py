from Channel import Channel
from Receiver import Receiver
from Sender import Sender


def main():
    sender = Sender()
    receiver = Receiver()
    channel = Channel()

    signal_length = int(input("Enter signal length:"))
    number_of_zeros = int(input("Enter number of zeros: "))

    sent_signal = sender.send_data(signal_length, number_of_zeros)
    sender.print_data()

    channel.receive(sent_signal)
    received_signal = channel.send()
    channel.print_data()

    receiver.receive_data(received_signal)
    receiver.print_data()


if __name__ == '__main__':
    main()
