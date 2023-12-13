import key_generator
import math
import typing
import random

def carmichael(n: int):
    """https://stackoverflow.com/questions/47761383/proper-carmichael-function"""
    n=int(n)
    k=2
    a=1
    alist: typing.List[int] = []

    while not ((math.gcd(a,n))==1):
        a=a+1

    while ((math.gcd(a,n))==1) & (a<=n) :
        alist.append(a)
        a=a+1
        while not ((math.gcd(a,n))==1):
            a=a+1

    timer=len(alist)
    while timer>=0:
        for a in alist:
            if (a**k)%n==1:
                timer=timer-1
                if timer <0:
                    break
                pass
            else:
                timer=len(alist)
                k=k+1
    return k

def show_values(p: int, q: int, e: int, d: int, n: int, phi_n: int):
    print ("Prime number P: ", p)
    print ("Prime number q: ", q)
    print ("Public Key: ", e)
    print ("Private Key: ", d)
    print ("n: ", n)
    print ("Phi of n: ", phi_n, " Secret")

p, q = key_generator.generate_prime_number(), key_generator.generate_prime_number()

if p == q:
    raise ValueError("Você conseguiu gerar 2 números iguais aleatóriamente. Falhou com sucesso!")

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) != 1: # gcd=greater common denometer     != not equal
     e = random.randint(3, phi_n - 1)

d = key_generator.mod_inverse(e, phi_n)

show_values(p, q, e, d, n, phi_n)

message = "Oi eu sou o goku!" # input("Enter your message to Encrypt ")
enconded_message = message.encode()
converted_message = int.from_bytes(enconded_message)
encrypted_msg = pow(converted_message, e, n)

decrypted_message_int = pow(encrypted_msg, d, n)
decrypted_message_bytes = decrypted_message_int.to_bytes((decrypted_message_int.bit_length() + 7) // 8, 'big')
decrypted_decoded_message = decrypted_message_bytes.decode()

print(f"Encrypted msg: {encrypted_msg}")
print(f"Decrypted msg: {decrypted_decoded_message}")