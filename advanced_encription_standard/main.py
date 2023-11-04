from aes import AES
import os 
from base64 import b64encode
from Crypto.Cipher import AES as Crypto_AES

def pad(text: bytes) -> ([bytes], int):
    """"Divide em segmentos de 128 bits"""
    byte_split = [text[i:i+16] for i in range(0, len(text), 16)]
    last_bit_len = len(byte_split[-1])

    if last_bit_len != 16:
        # Preenche o ultimo array com o ultimo byte
        number_of_missing_bytes = 16 - last_bit_len
        last_byte = byte_split[-1][-1:] * number_of_missing_bytes
        
        byte_split[-1] = byte_split[-1] + last_byte

    return byte_split, number_of_missing_bytes

if __name__ == "__main__":
    # Modo CTR teste
    text: str = 'qwertyuiopasdfghqwertyuiopasdfghabc' # input('Insira um texto para ser cifrado: ')
    key: str = 'asdfghjklzxcvbnm' # input('Insira uma chave (16 caracteres): ')
    rounds: int = 10 # input('Insira a quantidade de rounds: ')
    
    if len(text) < 16:
        raise ValueError("O texto deve ter mais que 16 characteres.")
    
    if len(key) != 16:
        raise ValueError("A chave deve ter 16 caracteres.")

    # Converte ambos em byte arrays
    text: bytes = bytearray.fromhex(text.encode('utf-8').hex())
    key: bytes = bytearray.fromhex(key.encode('utf-8').hex())

    # Faz o padding do texto caso seja maior 
    padded, pad_value = pad(text)
    
    # Encripta e desencripta
    cryptodome_aes = Crypto_AES.new(key=key, mode=Crypto_AES.MODE_ECB)
    cipher: AES = AES(key, rounds=10)

    encripted_result: [bytes] = []
    decripted_result: [bytes] = []
    final_decripted_result: bytes = b''
    final_encripted_result: bytes = b''

    cryptodome_encripted_result: [bytes] = []
    cryptodome_decripted_result: [bytes] = []
    cryptodome_final_decripted_result: bytes = b''
    cryptodome_final_encripted_result: bytes = b''

    for x in padded:
        # Nossa implementação
        encripted = cipher.encript(x)
        decripted = cipher.decript(encripted)

        # Implementação do cryptodome
        cryptodome_encripted = cryptodome_aes.encrypt(x)
        cryptodome_decripted_value = cryptodome_aes.decrypt(cryptodome_encripted)

        # Tranformamos em bytearray pra poder lidar melhor dps
        encripted_result.append(encripted) 
        decripted_result.append(decripted)

        cryptodome_encripted_result.append(cryptodome_encripted)
        cryptodome_decripted_result.append(cryptodome_decripted_value)

    # Monta os bytes novamente
    for value, cryptodome_value in zip(encripted_result, cryptodome_encripted_result):
        final_encripted_result += value
        cryptodome_final_encripted_result += cryptodome_value
    
     
    for value, cryptodome_value in zip(decripted_result, cryptodome_decripted_result):
        final_decripted_result += value  
        cryptodome_final_decripted_result += cryptodome_value

    # Retira o valor acrescentado no pad
    final_decripted_result = final_decripted_result[:-pad_value]
    final_encripted_result = final_encripted_result[:-pad_value]
    cryptodome_final_decripted_result = cryptodome_final_decripted_result[:-pad_value]
    cryptodome_final_encripted_result = cryptodome_final_encripted_result[:-pad_value]

    # Garantes que a nossa implementação está como a do cryptodome
    assert(final_decripted_result == cryptodome_final_decripted_result)
    assert(final_encripted_result == cryptodome_final_encripted_result)

