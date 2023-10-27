from dataclasses import dataclass
from consts import S_BOX, INVERSE_S_BOX
class AES:
    def __init__(self, key: str, text: str, rounds: int):
        self.key: bytes = bytearray.fromhex(key)
        self.text: bytes = bytearray.fromhex(text)
        self.rounds: int = rounds
    
    def encript(self) -> bytes:
        state = self.__get_state(self.text)
        key_schedule = self.__key_expansion(self.rounds)
        self.__add_round_key(state, key_schedule, round=0)

        for round in range(1, self.rounds):
            self.__sub_bytes(state)
            self.__shift_rows(state)
            self.__mix_columns(state)
            self.__add_round_key(state, key_schedule, round)

        self.__sub_bytes(state)
        self.__shift_rows(state)
        self.__add_round_key(state, key_schedule, round=self.rounds)

        cipher = self.__get_bytes(state)

        return cipher


    def decript(self, cipher_text: bytes) -> bytes:
        state = self.__get_state(cipher_text)
        key_schedule = self.__key_expansion(self.rounds)
        self.__add_round_key(state, key_schedule, round=self.rounds)

        for round in range(self.rounds - 1, 0, -1):
            self.__inv_shift_rows(state)
            self.__inv_sub_bytes(state)
            self.__add_round_key(state, key_schedule, round)
            self.__inv_mix_columns(state)

        self.__inv_shift_rows(state)
        self.__inv_sub_bytes(state)
        self.__add_round_key(state, key_schedule, round=0)

        text = self.__get_bytes(state)

        return text

    ### Metodos privados

    def __xtime(self, byte: int) -> int:
        """
        Exemplo:

        TODO:Encontrar bom exemplo
        """
        if byte & 0x80:
            return ((byte << 1) ^ 0x1b) & 0xff
        return byte << 1

    def __mix_columns(self, state: [int]):
        """
        Faz a mixagem de colunas. Exemplo:

        db 13 53 45 -> 8e 4d a1 bc

        https://en.wikipedia.org/wiki/Rijndael_MixColumns
        """
        for row in state:
            first_col = row[0]
            all_xor = row[0] ^ row[1] ^ row[2] ^ row[3]
            row[0] ^= all_xor ^ self.__xtime(row[0] ^ row[1])
            row[1] ^= all_xor ^ self.__xtime(row[1] ^ row[2])
            row[2] ^= all_xor ^ self.__xtime(row[2] ^ row[3])
            row[3] ^= all_xor ^ self.__xtime(first_col ^ row[3])

    def __shift_rows(self, state: [[int]]):
        """
        Faz uma rotação de todo o estado, semelhante ao que fazemos em rotate_word
        [
            [0x00, 0x01, 0x02, 0x03],
            [0x04, 0x05, 0x06, 0x07],
            [0x08, 0x09, 0x0A, 0x0B],
            [0x0C, 0x0D, 0x0E, 0x0F]
        ]

        A matrix acima, vira a matrix abaixo:

        [
            [0x00, 0x01, 0x02, 0x03],
            [0x05, 0x06, 0x07, 0x04],
            [0x0A, 0x0B, 0x08, 0x09],
            [0x0F, 0x0C, 0x0D, 0x0E]
        ]

        Obs: não retorna nada pois estamos modificando a referencia do estado
        """
        state[0][1], state[1][1], state[2][1], state[3][1] = state[1][1], state[2][1], state[3][1], state[0][1]
        state[0][2], state[1][2], state[2][2], state[3][2] = state[2][2], state[3][2], state[0][2], state[1][2]
        state[0][3], state[1][3], state[2][3], state[3][3] = state[3][3], state[0][3], state[1][3], state[2][3]
    
    def __sub_bytes(self, state: [[int]]):
        """
        Substituindo os bytes pelos valores da SBOX

        Obs: não retorna nada pois estamos modificando a referencia do estado
        """
        for row in range(len(state)):
            state[row] = [S_BOX[state[row][col]] for col in range(len(state[0]))]

    def __add_round_key(self, state: [[int]], key_schedule: [[[int]]], round: int):
        """
        Fazendo o bitwise XOR entre o stado e a chave

        Obs: não retorna nada pois estamos modificando a referencia do estado
        """
        round_key = key_schedule[round]
        range_value = range(len(state))
        for row in range_value:
            result = [] 

            for col in range(len(state[0])):
                result.append(state[row][col] ^ round_key[row][col])

            state[row] = result
    
    def __key_expansion(self, rounds: int = 1) -> [[[int]]]:
        """"
        Gera as varias chaves para usar nos rounds
        https://en.wikipedia.org/wiki/AES_key_schedule 
        """
        key_length = len(self.key) // 4
        number_of_words: int = 4
        key_matrix = self.__get_state(self.key)
        range_value = range(key_length, number_of_words * (rounds + 1)) 

        for round_number in range_value:
            temp = key_matrix[round_number - 1]
            
            if round_number % key_length == 0:
                first_bytes = self.__sub_word(self.__word_rotation(temp))
                second_bytes = self.__round_constant(round_number // key_length)
                temp = self.__xor_bytes(first_bytes, second_bytes)
            elif key_length > 6 & round_number % key_length == 4:
                temp = self.__sub_word(temp)

            key_matrix.append(self.__xor_bytes(key_matrix[round_number - key_length], temp))

        return [key_matrix[i*4:(i+1)*4] for i in range(len(key_matrix) // 4)]

    def __round_constant(self, i: int):
        """
        https://en.wikipedia.org/wiki/AES_key_schedule 
        """
        lookup_bytes = bytearray.fromhex('01020408102040801b36')
        return bytes([lookup_bytes[i-1], 0, 0, 0])

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
        return word[1:] + word[:1]

    def __get_state(self, data: bytes) -> [[int]]:
        """
        Divide os 16 bytes bytes em uma matrix 4x4. Exemplo:

        [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F]

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

    ### Inversas

    def __inv_shift_rows(self, state: [[int]]) -> [[int]]:
        """
        Faz uma rotação de todo o estado, semelhante ao que fazemos em rotate_word
        [
            [0x00, 0x01, 0x02, 0x03],
            [0x05, 0x06, 0x07, 0x04],
            [0x0A, 0x0B, 0x08, 0x09],
            [0x0F, 0x0C, 0x0D, 0x0E]
        ]

        A matrix acima, vira a matrix abaixo:

        [
            [0x00, 0x01, 0x02, 0x03],
            [0x04, 0x05, 0x06, 0x07],
            [0x08, 0x09, 0x0A, 0x0B],
            [0x0C, 0x0D, 0x0E, 0x0F]
        ]

        Obs: não retorna nada pois estamos modificando a referencia do estado
        """
        state[1][1], state[2][1], state[3][1], state[0][1] = state[0][1], state[1][1], state[2][1], state[3][1]
        state[2][2], state[3][2], state[0][2], state[1][2] = state[0][2], state[1][2], state[2][2], state[3][2]
        state[3][3], state[0][3], state[1][3], state[2][3] = state[0][3], state[1][3], state[2][3], state[3][3]

    def __inv_sub_bytes(self, state: [[int]]) -> [[int]]:
        for row in range(len(state)):
            state[row] = [INVERSE_S_BOX[state[row][col]] for col in range(len(state[0]))]


    def __xtimes_0e(self, b):
        # 0x0e = 14 = b1110 = ((x * 2 + x) * 2 + x) * 2
        return self.__xtime(self.__xtime(self.__xtime(b) ^ b) ^ b)


    def __xtimes_0b(self, b):
        # 0x0b = 11 = b1011 = ((x*2)*2+x)*2+x
        return self.__xtime(self.__xtime(self.__xtime(b)) ^ b) ^ b


    def __xtimes_0d(self, b):
        # 0x0d = 13 = b1101 = ((x*2+x)*2)*2+x
        return self.__xtime(self.__xtime(self.__xtime(b) ^ b)) ^ b


    def __xtimes_09(self, b):
        # 0x09 = 9  = b1001 = ((x*2)*2)*2+x
        return self.__xtime(self.__xtime(self.__xtime(b))) ^ b


    def __inv_mix_column(self, col: [int]):
        c_0, c_1, c_2, c_3 = col[0], col[1], col[2], col[3]

        col[0] = self.__xtimes_0e(c_0) ^ self.__xtimes_0b(c_1) ^ self.__xtimes_0d(c_2) ^ self.__xtimes_09(c_3)
        col[1] = self.__xtimes_09(c_0) ^ self.__xtimes_0e(c_1) ^ self.__xtimes_0b(c_2) ^ self.__xtimes_0d(c_3)
        col[2] = self.__xtimes_0d(c_0) ^ self.__xtimes_09(c_1) ^ self.__xtimes_0e(c_2) ^ self.__xtimes_0b(c_3)
        col[3] = self.__xtimes_0b(c_0) ^ self.__xtimes_0d(c_1) ^ self.__xtimes_09(c_2) ^ self.__xtimes_0e(c_3)


    def __inv_mix_columns(self, state: [[int]]) -> [[int]]:
        for row in state:
            self.__inv_mix_column(row)

if __name__ == "__main__":
    cipher = AES(key='000102030405060708090a0b0c0d0e0f', text='00112233445566778899aabbccddeeff', rounds=10)
    encripted = cipher.encript()
    decripted = cipher.decript(encripted)
    expected_ciphertext = bytearray.fromhex('69c4e0d86a7b0430d8cdb78070b4c55a')
    expected_text = bytearray.fromhex('00112233445566778899aabbccddeeff')

    assert (encripted == expected_ciphertext)
    assert (decripted == expected_text)
