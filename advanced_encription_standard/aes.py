from dataclasses import dataclass
class AES:
    def __init__(self, key: str, text: str, rounds: int):
        self.key = bytearray.fromhex(key)
        self.text = bytearray.fromhex(text)
        self.rounds = rounds
    
    def encript(self):
        state = self.__get_state()
        recovered = self.__get_bytes(state)

        print(state)
        print(recovered)
        pass        

    def decript(self):
        pass

    ### Metodos privados

    def __get_state(self) -> [[int]]:
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
        data = self.text
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
