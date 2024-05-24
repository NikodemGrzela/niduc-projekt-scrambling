import random
# Scrambler/descrambler addytywny DBE
# Źródła: 
# - https://en.wikipedia.org/wiki/Scrambler
# Scrambling polega na wykonaniu operacji xor według schematu
# Z wartościami w rejestrach o indeksach takich jak potęgi wielomianu
# którym jest zdefiniowany scrambler.

# Użyty wielomian 1 + z^-14 + z^-15
# Stan początkowy LSFR: {1,0,0,1,0,1,0,1,0,0,0,0,0,0,0}

class DBEScrambler:
    def __init__(self):
        self.initialState = [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0]
        self.LFSR = self.initialState.copy()      # linear-feedback shift register
        self.syncFrame = 14  # syncWord pojawia sie w data input co 15 znakow

    # Zgodnie ze schematem:
    # https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Scrambler_randomizer_additive.png/350px-Scrambler_randomizer_additive.png
    def scramble(self, signal):
        output_signal = []

        self.LFSR = self.initialState.copy()

        reset_count = 0
        for input_bit in signal:
            if reset_count % self.syncFrame  == 0:
                self.LFSR = self.initialState.copy()
            reset_count += 1
            feedback = self.LFSR[13] ^ self.LFSR[14]
            output_bit = int(input_bit) ^ feedback
            self.LFSR = [feedback] + self.LFSR[:-1]
            output_signal.append(output_bit)
            
        return output_signal


    def descramble(self, signal):
        return self.scramble(signal)

    def print_data(self):
        print("DBE Scrambler:")
        print("Scrambler polynomial: 1 + z^-14 + z^-15") 
        print()