from dataclasses import dataclass
class AES:
    def __init__(key: str, text: str, rounds: int):
        # Precisamos dividir o texto em vários segmentos
        self.key = bytearray.fromhex(key)
        self.text = bytearray.fromhex(text)
        self.rounds = rounds
    
    def encript(self):
        state = get_state()
        pass        

    def get_state(self):
        pass

if __name__ == "__main__":

    plaintext = bytearray.fromhex('00112233445566778899aabbccddeeff')
    key = bytearray.fromhex('000102030405060708090a0b0c0d0e0f')
    cipher = AES()
    # expected_ciphertext = bytearray.fromhex('69c4e0d86a7b0430d8cdb78070b4c55a')
    # ciphertext = aes_encryption(plaintext, key)
    # recovered_plaintext = aes_decryption(ciphertext, key)

    # assert (ciphertext == expected_ciphertext)
    # assert (recovered_plaintext == plaintext)
