import key_generator
import math



def get_public_key(e: int = 65537):
    """
    A chave publica é composta do resultado da multiplicação de dois numeros primos distintos, 'p' e 'q' e de um expoente 'e'.

    https://datatracker.ietf.org/doc/html/rfc8017#section-3.1
    """
    p = key_generator.generate_prime_number()
    q = key_generator.generate_prime_number()
    n = p * q
    lambda_n =  math.lcm(p - 1, q - 1)
    test = math.gcd(e, lambda_n) == 1

    if not test: raise ValueError("Os valores escolhidos para 'p', 'q' e 'e' não passam no teste") 

    return n, e

# TODO: chave privada ainda n funciona
def get_private_key(d: int = 65537, e: int = 65537):
    """"
    A chave privada, assim como a publica, 
    é composta do resultado da multiplicação de dois numeros primos distintos, 'p' e 'q' e de um expoente 'd'.

    https://datatracker.ietf.org/doc/html/rfc8017#section-3.2
    """
    p = key_generator.generate_prime_number()
    q = key_generator.generate_prime_number()
    n = p * q
    lambda_n =  math.lcm(p - 1, q - 1)
    test = (e * d) % lambda_n == 1 

    if not test: raise ValueError("Os valores escolhidos para 'p', 'q' e 'd' não passam no teste")  

    return n, d

def encrypt(msg: str):
    rsa_public_modulus, rsa_public_exponent = get_public_key()
    rsa_private_modulus, rsa_private_exponent = get_private_key()


if __name__ == "__main__":
    encrypt("teste")