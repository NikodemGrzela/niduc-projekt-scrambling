import random

# Scrambler/descrambler multiplikatywny użyty w rekomendacji V.34
# Źródła: 
# - https://en.wikipedia.org/wiki/Scrambler
# - https://people.ece.ubc.ca/~edc/4340.fall2014/lectures/lec12.pdf
# Użyty wielomian 1 + z^-18 + z^-23
# Scrambling polega na wykonaniu operacji xor według schematu
# Z wartościami w rejestrach o indeksach takich jak potęgi wielomianu
# którym jest zdefiniowany scrambler.
class V34Scrambler:
    def __init__(self):
        self.scramble_register = [random.randint(0, 1) for _ in range(23)]
        self.descramble_register = self.scramble_register.copy()

    # Zgodnie ze schematem
    # https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Scrambler_randomizer_multiplicative_scrambler.png/525px-Scrambler_randomizer_multiplicative_scrambler.png
    def scramble(self, signal):
        output_signal = []
        for input_bit in signal:
            feedback = self.scramble_register[17] ^ self.scramble_register[22]
            output_bit = int(input_bit) ^ feedback
            self.scramble_register = [output_bit] + self.scramble_register[:-1]
            output_signal.append(output_bit)

        return output_signal


    # Zgodnie ze schematem
    # https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Scrambler_randomizer_multiplicative_descrambler.png/525px-Scrambler_randomizer_multiplicative_descrambler.png
    def descramble(self, signal):
        output_signal = []
        for input_bit in signal:
            feedback = self.descramble_register[17] ^ self.descramble_register[22]
            output_bit = int(input_bit) ^ feedback
            self.descramble_register = [input_bit] + self.descramble_register[:-1]
            output_signal.append(output_bit)

        return output_signal
        
    def print_data(self):
        print("V34 Scrambler:")
        print("Scrambler polynomial: 1 + z^-18 + z^-23")
        print()