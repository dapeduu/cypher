from aes import AES
import os 
from base64 import b64encode

def pad(text: bytes):
    """"Divide em segmentos de 128 bits"""
    byte_split = [text[i:i+16] for i in range(0, len(text), 16)]
    last_bit_len = len(byte_split[-1])

    if last_bit_len != 16:
        # Preenche o ultimo array com bits aleatorios
        number_of_missing_bytes = 16 - last_bit_len
        last_byte = byte_split[-1][-1:] * 13
        
        byte_split[-1] = byte_split[-1] + last_byte

    return byte_split

if __name__ == "__main__":
    # Modo CTR teste
    text = 'qwertyuiopasdfghqwertyuiopasdfghabc' # input('Insira um texto para ser cifrado: ')
    key = 'asdfghjklzxcvbnm' # input('Insira uma chave (16 caracteres): ')
    rounds = 10 # input('Insira a quantidade de rounds: ')

    if len(text) < 16:
        raise ValueError("O texto deve ter mais que 16 characteres.")
    
    if len(key) != 16:
        raise ValueError("A chave deve ter 16 caracteres.")

    # Converte ambos em byte arrays
    text = bytearray.fromhex(text.encode('utf-8').hex())
    key = bytearray.fromhex(key.encode('utf-8').hex())

    # Faz o padding do texto caso seja maior 
    padded = pad(text)
    
    # Encripta e desencripta
    cipher = AES(key, rounds=10)
    encripted_result = []
    decripted_result = []

    for x in padded:
        encripted = cipher.encript(x)
        decripted = cipher.decript(encripted)

        # Tranformamos em bytearray pra poder lidar melhor dps
        encripted_result.append(encripted) 
        decripted_result.append(decripted)

    print(encripted_result)
    print(decripted_result)
