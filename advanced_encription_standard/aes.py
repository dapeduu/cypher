from dataclasses import dataclass
from consts import S_BOX
class AES:
    def __init__(self, key: str, text: str, rounds: int):
        self.key: bytes = bytearray.fromhex(key)
        self.text: bytes = bytearray.fromhex(text)
        self.rounds: int = rounds
    
    def encript(self):
        state = self.__get_state()

        pass        

    def decript(self):
        pass

    ### Metodos privados

    def __key_expansion(self, rounds: int = 1) -> [[[int]]]:
        """"
        Gera as varias chaves para usar nos rounds

        """
        nk = len(self.key)
        number_of_words: int = 4
        first_key_matrix = self.__get_state(self.key)
        range_value = range(nk, number_of_words * (rounds + 1) ) 
        result = [first_key_matrix]

        for round_number in range_value:
            temp = first_key_matrix[round_number - 1]
            
            if round_number % nk == 0:
                first_bytes = self.__sub_word(self.__word_rotation(temp))
                second_bytes = self.__round_constant(round_number // nk)
                temp = self.__xor_bytes(first_bytes, second_bytes)
            elif nk > 6 & round_number % nk == 4:
                temp = self.__sub_word(temp)

            result.append(xor_bytes(result[round_number - nk], temp))

        return result

    def __round_constant(self, i: int):
        """

        https://en.wikipedia.org/wiki/AES_key_schedule 
        """
        lookup_bytes = bytearray.fromhex('01020408102040801b36')
        return bytes([rcon_lookup[i-1], 0, 0, 0])

    def __sub_word(self, word: [int]):
        """
        Substitui os bytes pelos bytes definidos na SBOX
        https://en.wikipedia.org/wiki/Rijndael_S-box
        """
        return bytes(S_BOX[i] for i in word)

    def __xor_bytes(self, bytes_a: bytes, bytes_b: bytes):
        """
        Faz o XOR entre os bytes
        https://en.wikipedia.org/wiki/Exclusive_or
        """
        return bytes([x ^ y for (x, y) in zip(bytes_a, bytes_b)])

    def __word_rotation(self, word: [int]) -> [int]:
        """
        Faz uma rotação na word. Exemplo:
        
        [0x00, 0x01, 0x02, 0x03]
        A word acima vira:
        [0x01, 0x02, 0x03, 0x00]
        """
        return [word[1:] + word[:1]]


    def __get_state(self, data: bytes) -> [[int]]:
        """
        Divide os 16 bytes bytes em uma matrix 4x4. Exemplo:

        O array acima vira a matrix abaixo:

        [
            [0x00, 0x01, 0x02, 0x03],
            [0x04, 0x05, 0x06, 0x07],
            [0x08, 0x09, 0x0A, 0x0B],
            [0x0C, 0x0D, 0x0E, 0x0F]
        ]
        """
        state = []

        for i in range(0, len(data), 4):
            # Divide os dados em pedacinhos de 4 bytes
            chunk = data[i:i+4]
            state.append(chunk)

        return state

    def  __get_bytes(self, state: [[int]]) -> bytes:
        """"
        Monta a matrix de bytes 4x4 novamente em um array. Exemplo

        [
            [0x00, 0x01, 0x02, 0x03],
            [0x04, 0x05, 0x06, 0x07],
            [0x08, 0x09, 0x0A, 0x0B],
            [0x0C, 0x0D, 0x0E, 0x0F]
        ]

        A matriz acima vira o array abaixo:

        [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
        """
        result = []
        size = range(len(state))

        for line in size:
            for column in size:
                result.append(state[line][column])

        return bytes(result)

if __name__ == "__main__":
    cipher = AES(key='000102030405060708090a0b0c0d0e0f', text='00112233445566778899aabbccddeeff', rounds=1)
    cipher.encript()

    # expected_ciphertext = bytearray.fromhex('69c4e0d86a7b0430d8cdb78070b4c55a')
    # ciphertext = aes_encryption(plaintext, key)
    # recovered_plaintext = aes_decryption(ciphertext, key)

    # assert (ciphertext == expected_ciphertext)
    # assert (recovered_plaintext == plaintext)
