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

# Links úteis
- https://pdf.sciencedirectassets.com/277348/1-s2.0-S1875389212X00063/1-s2.0-S1875389212005822/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIBKHKQEn%2BtX0TOsWMDGK5SHTNqyAtknmuqR7KMlrw8WcAiEAga5AO9TDtWdiODvRM5CR7pdBDL7kOVMLc1YCFVkt338qvAUI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAFGgwwNTkwMDM1NDY4NjUiDBKzNdsWoDUzXNqBaCqQBU4q0Irxv9iR%2BAM26PHtzvG9Arqk7UHFZImEEWQkRkwPyVp88gUxz4X%2F1QwzK0GudIFytiJdHW7RDcsNU1ssgQrPahlB%2BKCMcFlltKrpd4%2FwyD61y9RR1Vr7L3ByJT1cnHPpZnJZn5DZeJlMq6bWHg8HmDxuMbx2lgSBAoWnN0HcgLY8Zi0%2Bug3GITGzEXI%2BOC9%2FNa%2B%2FOS%2FURwHbhMZTyBIxCHu63uisanpVG0xmkJDXb3jtI0FGY4uciuaHFRB9K7CDGKoFsGj4VIbbU8lb3Iie3%2FmQEiQgTWvUdORbt6Q5c6Y00%2BCKrhA4en65r1ndOKyovw7g048JcE%2Fd5nMvf68%2BthjGWPpgrs%2B5rN6Cc4HuxDUY9jQRiVsHYhedIJOIPGJZ6Euz%2BZwDHS4XufytVtCGOS70vH6tu2mWmrobLTPBFH74BXSguTspgamIJefQDtdaxP9GepOc%2BxZR1gg3SXPY%2Bra3ZejnSTFlR7qH7zRlFT56%2BRidE309xElQ14u96k4B7Qrz743DODOs6LPEfv%2Bz%2Fr7YOqt196vNZ6oSg5bQliAeyDfNp0mueqQncr6TeEXRclGdRAYFrIghdoX2G3yIgitC2Z%2F6PoBjBZgrfgwR2kLrvc6Ycrsu02PVfDfcSxedXxaBtqvJEmVw%2FMU%2Fn0poNxYHgk5eU4F3gYli0EfdEdIcw6ELY3dvDtXf54lloG%2BKLqd75CsOqzddRi7V9Dh3Vpzo7jaJ%2FP5XqW3AxVx2fKfy5fAZjVLdTMEWgNbwV76UPNGUPKfEdCexdUnRV0DaLElF4GGNHFmxpR%2B3m5HUrcaFeA7IPUvjBy5xQdshQqjKvWC1uryU8oxeMB96JRK9KfU6GgHZW7scx4kPa2Q9MO3Qy6kGOrEBfnM2phbWTFk3H%2BYF%2FkQ23jovKwdIf3w9H0Gqcf0a%2FQ5BXA0SlaSglBzUhpqXo1KXKvtaLfoK9HjoWbHU4w6hr70HfWMGgWbkBTnKAbUGmIqpQnFedP3mRIVzZ6sAyGruC%2FNdfCQKxxGXk8FFh8b4uU9Ufxcmqk0OmM2ZWH9p4f%2B8f9QBj4kqXNs9QoD0lWdZsyrqHlgwqrNr0Gr2vKIoDOOBOoHmU9ozt4j9LkukwVRG&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20231020T224546Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY347TFOBP%2F20231020%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=eb5a36c0c75546c5b72238e076873b742ba3b16b660d870a80fc9f8b88015996&hash=2d5c37afc531178b9847cc9da803acf70bc91b330e6e27f9d913c08e02f26c7c&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1875389212005822&tid=spdf-c57dcc50-b56f-4566-be6f-1bd97bcdcc3c&sid=dde0d3314791604f0a0aeaf375f16840f154gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=041157515a5307065e54&rr=8194cb040ae55a30&cc=br

- https://en.wikipedia.org/wiki/Rijndael_S-box
