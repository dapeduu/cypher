from cipher_and_decipher import decipher, cipher, generate_key

text = "TESTEOILA"
keyword = "senha"
key = generate_key(text, keyword)

encripted = cipher(text, key)
decripted = decipher(encripted, key)

print(f"Encripted: {encripted}")
print(f"Decripted: {decripted}")
