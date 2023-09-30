ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def encrypt(plaintext,key):
    ciphertext = ''

    for i in range(len(plaintext)):
        p = ALPHABET.index(plaintext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p + k) % 26
        ciphertext += ALPHABET[c]

    return ciphertext

def decrypt(ciphertext,key):
    plaintext = ''

    for i in range(len(ciphertext)):
        p = ALPHABET.index(ciphertext[i])
        k = ALPHABET.index(key[i%len(key)])
        c = (p - k) % 26
        plaintext += ALPHABET[c]

    return plaintext

plaintext = 'GEEKSFORGEEKS'
key = 'AYUSH'
expected_cipher_text = 'GCYCZFMLYLEIM'

gotten_cipher_text = encrypt(plaintext, key)
gotten_plain_text = decrypt(gotten_cipher_text, key)

print((plaintext, key, expected_cipher_text))
print((gotten_cipher_text, gotten_plain_text))

