from consts import ALPHABET

def encrypt(plaintext: str, key: str):
    plaintext = plaintext.lower()
    key = key.lower()

    ciphertext = ''

    print("encrypt")
    for i in range(len(plaintext)):
        if __ignore_char(plaintext[i]):
            ciphertext += plaintext[i]
            continue

        text_letter_index = ALPHABET.index(plaintext[i])
        key_letter_index = ALPHABET.index(key[i % len(key)])
        resulting_letter_index = (text_letter_index + key_letter_index) % 26
        ciphertext += ALPHABET[resulting_letter_index]

        print(f"{plaintext[i]} {key[i % len(key)]} = {ALPHABET[resulting_letter_index]}")
    print()

    return ciphertext

def decrypt(ciphertext: str, key: str):
    ciphertext = ciphertext.lower()
    key = key.lower()

    plaintext = ''

    print("decrypt")
    for i in range(len(ciphertext)):
        if __ignore_char(ciphertext[i]):
             plaintext += ciphertext[i]
             continue

        text_letter_index = ALPHABET.index(ciphertext[i])
        key_letter_index = ALPHABET.index(key[i % len(key)])
        resulting_letter_index = (text_letter_index - key_letter_index) % 26
        plaintext += ALPHABET[resulting_letter_index]

        print(f"{plaintext[i]} {key[i % len(key)]} = {ALPHABET[resulting_letter_index]}")
    print()

    return plaintext

def __ignore_char(char: str):
    space = char == ' '
    numeric = char.isnumeric()
    special = char in 'ç!@#$%^&*()-+.,'

    return space or numeric or special