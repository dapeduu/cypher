import random

# n= p.q
#phi(n) = phi(p.q)=phi(p).phi(q) = (p-1). (q-1)
#phi(n) = (p-1.q-1)


def miller_rabin(number: int, rounds: int):
    """
    A implementação utiliza o Teste de Primalidade de Miller-Rabin.
    O número ideal de iterações para este teste é 40.
    Consulte http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    para justificativa.

    Se o número for par, é um número composto.

    Retorna verdadeiro se n passar no teste.

    Fonte: https://gist.github.com/Ayrx/5884790
    """

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    r, s = 0, number - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(rounds):
        a = random.randrange(2, number - 1)
        x = pow(a, s, number)
        if x == 1 or x == number - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, number)
            if x == number - 1:
                break
        else:
            return False
            
    return True

def generate_prime_candidate(length: int):
    """
    Gera um numero aleátorio, e aplica mascára para que o bit mais significativo e o menos significativo sejam 1
    """
    p = random.getrandbits(length)
    # Aplica apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1  

    return p


def generate_prime_number(length: int = 1024):
    """ 
    Gera números aleatórios até que um passe no teste de Miller-Rabin
    """
    p = 4
    # keep generating while the primality test fail
    while not miller_rabin(p, 128):
        p = generate_prime_candidate(length)

    return p

def mod_inverse(e: int, phi: int):
    """
    Gera o módulo inverso de um número.
    """

    for d in range (3, phi):

        if (d * e) % phi == 1:

            return d 

    raise ValueError ("Mod_inverse does not exist!")
