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

        receiver.compare(sender.get_signal())



if __name__ == '__main__':
    main()

