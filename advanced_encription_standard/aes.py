from dataclasses import dataclass
from consts import S_BOX, INVERSE_S_BOX

@dataclass
class AES:
    """Implementação do Advanced Encription Standard"""
    key: bytes
    text: bytes
    

    def padding(text: str, block_size: int) -> bytes:
        """
        Dividir o texto em blocos de 16 bytes ou 128 bits.
        """ 
        # Transforma o texto em bytes
        text = bytes(text)
        # Calcula o numero de bytes
        padding_size = block_size - (len(text) % block_size)
        # Cria um byte com o tamanho correto
        padding = bytes([padding_size] * padding_size)
        # Adiciona o padding ao texto original
        padded_text = text + padding
    
    return padded_text

    def key_expansion(key: str):
        """
        Recebe a chave e gera outras
        de acordo com a tabela abaixo:

        | Tamanho da Chave (bits) | Quantidade de Rounds  |
        |-------------------------|-----------------------|
        | 128                     | 10                    |
        | 192                     | 12                    |
        | 256                     | 14                    |
        """
        keys = []

        return keys

    def add_round_key(key: str, text: str):
        """
        Recebe uma chave e um texto e cifra o texto
    um exemplo seria a operação XOR bit a bit
        """
        ciphered_text = ""

        return ciphered_text

    def sub_bytes(cipher_text: str):
        """
        Substituir os bits por outros de acordo com algum padrão definido.
        Esse documento mostra uma tabela de substituição:
        https://www.ime.usp.br/~rt/cranalysis/AESSimplified
        """
        sub_bytes_result = ""

        return sub_bytes_result

    def shift_rows(cipher_text: str):
        """
        Fazer o shift das linhas
        """
        rows_shifted = ""

        return rows_shifted

    def mix_columns(cipher_text: str):
        """
        Fazer a mixagem das colunas
        """
        columns_mixed = ""

        return columns_mixed