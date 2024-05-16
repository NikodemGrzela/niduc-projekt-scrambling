from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
#https://www.allaboutcircuits.com/technical-articles/understanding-security-keys-in-bluetooth-low-energy/
#https://infocenter.nordicsemi.com/index.jsp?topic=%2Fcom.nordic.infocenter.nrf52832.ps.v1.1%2Fccm.html
class BLEScrambler:
    def __init__(self):
        self.key=get_random_bytes(16)

    def scramble(self,signal):
        scrambled_signal = []
        
       #licznik 8 bajtowy
        counter = b'\x00\x00\x00\x00\x00\x00\x00\x00'

        # Inicjalizacja szyfru AES w trybie CTR
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=counter)

        # Szyfrowanie danych
        signal_bits = cipher.encrypt(BLEScrambler.bits_to_bytes(signal))
        scrambled_signal = BLEScrambler.bytes_to_bits(signal_bits)

        return scrambled_signal

    def descramble(self,signal):
        descrambled_signal= []
       
        counter = b'\x00\x00\x00\x00\x00\x00\x00\x00'
        cipher = AES.new(self.key, AES.MODE_CTR, nonce=counter)
        descrambled_signal_bits = cipher.decrypt(BLEScrambler.bits_to_bytes(signal))
        
        return BLEScrambler.bytes_to_bits(descrambled_signal_bits)

   #dopelnienie do 8 i transformacja tablicy bitów na bajty
    def bits_to_bytes(bit_array):
    
        if len(bit_array) % 8 != 0:
            bit_array += [0] * (8 - len(bit_array) % 8)

        byte_chunks = [bit_array[i:i+8] for i in range(0, len(bit_array), 8)]
        bytes_result = bytearray([int(''.join(map(str, chunk)), 2) for chunk in byte_chunks])

        return bytes_result
#zamiana bajtów na tablice z bitami
    def bytes_to_bits(byte_array):
  
        bits = []

   
        for byte in byte_array:
            bits.extend([int(bit) for bit in format(byte, '08b')])

        return bits
    
    def print_data(self):
        print("Scramble BLE:")
        print("AES CTR")
        print()