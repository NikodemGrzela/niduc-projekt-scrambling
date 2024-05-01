from Sender import Sender
from Receiver import Receiver



def main():
    while True:
        sender = Sender()
        receiver = Receiver()
        receiver.receive_data(sender.send_data())
        sender.print_data()
        receiver.print_data()




if __name__ == '__main__':
    main()

