import random

# Użyty wielomian 1 + z^-4 + z^-7
# Stan początkowy LSFR: wartosc zegara centralnego rozszerzona o 1- tu losowana 

class BLEScrambler:
    def __init__(self):
        self.initialState = [random.choice([0, 1]) for _ in range(7)]
        
       
   
    def scramble(self, signal):
        output_signal = []
        self.LFSR = self.initialState.copy()
       

        
        for input_bit in signal:
               #wstawienie feedback na pozycje 4, przesunięcie od 0 do 3 w prawo, od 4 do 5 w prawo, bit 6 na pozycje 0     
            #https://www.allaboutcircuits.com/uploads/articles/WhiteningEncoder_optimized.gif
            feedback = self.LFSR[3] ^ self.LFSR[6] # bit wejsciowy xorowany z bitem 6
            output_bit = int(input_bit) ^ self.LFSR[6]
        
            self.LFSR = self.LFSR[6:]+self.LFSR[0:3]+[feedback]+self.LFSR[4:6]
            output_signal.append(output_bit)
            
        return output_signal


    def descramble(self, signal):
        return self.scramble(signal)

    def print_data(self):
        print("BLE Scrambler:")
        print("Scrambler polynomial: 1 + z^-4 + z^-7") 
        print()