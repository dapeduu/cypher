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

def show_result(msg: str, encripted_msg: str):
    print("Original message: ", msg)
    print("Encripted message:", encripted_msg)

p, q = key_generator.generate_prime_number(), key_generator.generate_prime_number()

if p == q:
    raise ValueError("Você conseguiu gerar 2 números iguais aleatóriamente. Falhou com sucesso!")

n = p * q
phi_n = (p-1) * (q-1)
e = random.randint(3, phi_n-1)

while math.gcd(e, phi_n) != 1: #gcd=greater common denometer     != not equal
     e = random.randint(3, phi_n - 1)

d = key_generator.mod_inverse(e, phi_n)

show_values(p, q, e, d, n, phi_n)

message = "Oi" # input("Enter your message to Encrypt ")
message_unicode = [ord(ch) for ch in message]

# (m ^ e) mod n = c 
ciphertext_list = [pow(ch, e, n) for ch in message_unicode]
print("Ciphertext generated.")
recovered_text_list = [pow(ch, d, n) for ch in ciphertext_list] 
print("Recovered text generated.")

recovered_text = "".join (chr(ch) for ch in recovered_text_list)
recovered_ciphertext = "".join (chr(ch) for ch in ciphertext_list)

show_result(message, recovered_ciphertext)