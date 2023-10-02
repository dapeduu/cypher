from collections import Counter
import re
from cipher_and_decipher import decrypt
from consts import PORTUGUESE_LETTER_FREQUENCY, ALPHABET


def calculate_index_of_coincidence(text: str):
    text = text.lower()  # Convert text to lowercase for case insensitivity
    text = re.sub(r'[^a-zA-Z]', '', text) # Only characters from a to z
    total_characters = len(text)

    # Initialize a dictionary to count the frequency of each letter
    letter_count = {}

    # Count the occurrences of each letter in the text
    for char in text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    # Calculate the Index of Coincidence
    ioc = 0.0
    for count in letter_count.values():
        ioc += (count * (count - 1)) / (total_characters * (total_characters - 1))

    return ioc, letter_count

def divide_text_by_key_length(text: str, key_length: int):
    text = re.sub(r'[^a-zA-Z]', '', text) # Only characters from a to z
    return [text[i::key_length] for i in range(key_length)]

def vigenere_crack(text: str):
    divided_texts = divide_text_by_key_length(text, key_length=5)
    possible_keys = []

    # Find the keys for each divided text
    for divided_text in divided_texts:
        ioc = calculate_index_of_coincidence(divided_text)
        most_common_letter = max(ioc[1], key=ioc[1].get)
        best_letter_index = (ord(most_common_letter) - ord('a')) % 26
        print(ALPHABET[best_letter_index])
        possible_keys.append(ALPHABET[best_letter_index])

    # Combine
    vigenere_key = "".join(possible_keys)

    return vigenere_key

# Example usage:
text = """
Pc sp, rn bfe wk pv, ekwh zd wds hfhohzzq
Svvekaf ktv Jcswhn we eka azyg pc jfibsi
Eka Gctqcg ryg Wfizzo cw zxpfrrhkij Qrnhlyh,
Kf kz wwyv Luig rrdebje d Osr zi pfffehsj,
Lqz pp zslcjtqc seo wdsd?
Hlhzzlp Ovrvhodvlua Vrxoah
"""

vigenere_key = vigenere_crack(text)
decripted = decrypt(text, vigenere_key)
print(vigenere_key)
print(decripted)
