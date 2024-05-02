from Sender import Sender
from Receiver import Receiver
from Channel import Channel


def main():
    while True:
        sender = Sender()
        receiver = Receiver()
        channel = Channel(sender,receiver)
        channel.receive(sender.send_data())
        receiver.receive_data(channel.send())
        sender.print_data()
        channel.print_data()
        receiver.print_data()




if __name__ == '__main__':
    main()

