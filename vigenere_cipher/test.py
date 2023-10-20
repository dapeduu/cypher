import re
import cipher_and_decipher

# Input

cipher_text = input("Ciphertext: ")
cipher_text = re.sub('[^a-zA-Z]+', '', cipher_text)
cipher_text = cipher_text.upper()

plain_text = input("Plaintext: ")
plain_text = re.sub('[^a-zA-Z]+', '', plain_text)
plain_text = plain_text.upper()

keyword =input("Keyword: ").upper()
key_size = cipher_text if cipher_text else plain_text

key = cipher_and_decipher.generate_key(key_size, keyword)

print(f'Original: {plain_text}')
print('=' * 30)

if cipher_text and keyword:
    decripted = cipher_and_decipher.decipher(cipher_text, key)
else:
    encripted = cipher_and_decipher.cipher(plain_text, key)
    decripted = cipher_and_decipher.decipher(encripted, key)
    
    print(f"Encripted: {encripted}")
    print('=' * 30)

print(f"Key: {key}")
print('=' * 30)
print(f"Decripted: {decripted}")


   