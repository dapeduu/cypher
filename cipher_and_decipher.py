from consts import ALPHABET

def encrypt(plaintext: str, key: str):
    plaintext = plaintext.lower()
    key = key.lower()

    ciphertext = ''

    for i in range(len(plaintext)):
        if __ignore_char(plaintext[i]):
            ciphertext += plaintext[i]
            continue

        p = ALPHABET.index(plaintext[i])
        k = ALPHABET.index(key[i % len(key)])
        c = (p + k) % 26
        ciphertext += ALPHABET[c]

    return ciphertext

def decrypt(ciphertext: str, key: str):
    ciphertext = ciphertext.lower()
    key = key.lower()

    plaintext = ''

    for i in range(len(ciphertext)):
        if __ignore_char(ciphertext[i]):
             plaintext += ciphertext[i]
             continue

        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i % len(key)])
        c = (p - k) % 26
        plaintext += ALPHABET[c]

    return plaintext

def __ignore_char(char: str):
    space = char == ' '
    numeric = char.isnumeric()
    special = char in 'ç!@#$%^&*()-+.,'

    return space or numeric or special