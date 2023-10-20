# Advanced Encription Standard

# Passo a passo

## Encriptar
- KeyExpansion
    - Expandimos a chave pelo número de rounds que queremos rodar
- AddRoundKey
    - É o processo de pegar o texto original e fazer a operação com a chave. Ex: XOR
- SubBytes
    - Após aplicar a chave vamos substituir os bits por outros de acordo com algum padrão definido
- ShiftRows 
    - Fazer um shift das linhas dependendo do seu numero. Ex:
    
    1234 4231

    5678 7856
- MixColumns
    - Combinamos os valores de cada coluna para gerar novos valores de colunas

Cada round é composto de:

KeyExpansion -> AddRoundKey -> SubBytes -> ShiftRows -> MixColumns -> AddRoundKey

Obs: MixColumns não ocorre no ultimo round

O tamanho da chave vai determinar a quantidade de rounds:

| Tamanho da Chave (bits) | Quantidade de Rounds |
|-------------------------|-----------------------|
| 128                     | 10                    |
| 192                     | 12                    |
| 256                     | 14                    |
