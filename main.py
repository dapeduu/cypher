from cipher_and_decipher import decrypt, encrypt



encripted = encrypt(plaintext="The quick brown fox jumps over treze lazy dogs.", key="senha")
decripted = decrypt(ciphertext=encripted, key="senha")

print(f"Encripted: {encripted}")
print(f"Decripted: {decripted}")