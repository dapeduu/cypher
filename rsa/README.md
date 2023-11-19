**RSA Signature Generator and Verifier**

Este projeto implementa um sistema de assinatura digital usando o algoritmo RSA (Rivest-Shamir-Adleman) em arquivos. Ele inclui a geração de chaves, cifração/decifração assimétrica RSA com OAEP, cálculo de hashes SHA-3, assinatura da mensagem e verificação.

# Estrutura do Projeto

O projeto está dividido em três partes principais:

1. **Parte I: Geração de Chaves e Cifra**
   - `key_generator.py`: Gera chaves RSA com p e q primos, cada um com no mínimo de 1024 bits.
   - `rsa_cipher.py`: Implementa cifração/decifração RSA usando OAEP.

2. **Parte II: Assinatura**
   - `hash_calculator.py`: Calcula o hash SHA-3 da mensagem em claro.
   - `sign.py`: Realiza a assinatura digital, cifrando o hash com a chave privada e formatando o resultado.

3. **Parte III: Verificação**
   - `verifyer.py`: Analisa o documento assinado, decifra a mensagem e a assinatura, e verifica se a assinatura é válida.

# Pré-requisitos

- Certifique-se de ter Python instalado (versão 3.6 ou superior).

# Como Usar

1. **Geração de Chaves:**
   A função `generate_prime_number` em `key_generator.py` gerará um par de chaves (pública e privada) e salvará os resultados em arquivos.

2. **Assinatura:**
   ```bash
   python sign.py
   ```
   Assina a mensagem e salva a assinatura em um arquivo.

3. **Verificação:**
   ```bash
   python verifyer.py -m <arquivo_mensagem> -a <arquivo_assinatura> -k <chave_publica>
   ```
   Verifica se a assinatura é válida para a mensagem dada.

# Considerações de Segurança

- Certifique-se de seguir as melhores práticas de segurança ao lidar com chaves privadas e públicas.
- Este projeto não abrange todos os aspectos de segurança; é recomendável revisar e ajustar de acordo com os requisitos específicos.

# Bibliotecas Utilizadas

- `hashlib`: Utilizada para cálculos de hash SHA-3.

# Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

# Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests com melhorias ou correções.