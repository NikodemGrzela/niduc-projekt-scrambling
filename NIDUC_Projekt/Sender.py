import random

class Sender:
    def __init__(self):
        pass

    def send_data(self):
        self.data = generate_data()
        return self.data

    def print_data(self):
        print(self.data)



def generate_data():
    #Ask user for 0/1 amount, length
    len = int(input("Enter signal length:"))
    number_of_zeros = int(input("Enter number of zeros: "))
    number_of_ones = len - number_of_zeros
    signal = number_of_ones * '1' + (number_of_zeros * '0')
    return scramble_string(signal)

def scramble_string(signal):
    char_list = list(signal)
    random.shuffle(char_list)
    scrambled_string = ''.join(char_list)
    return scrambled_string