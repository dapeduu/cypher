from collections import Counter
import re
from cipher_and_decipher import vigenere_decrypt

def calculate_ic(text):
    # Calculate the Index of Coincidence (IC)
    text = re.sub(r'[^a-zA-Z]', '', text)  # Remove non-alphabetic characters
    n = len(text)
    if n <= 1:
        return 0.0
    freq_count = Counter(text)
    ic = sum((freq * (freq - 1)) for freq in freq_count.values()) / (n * (n - 1))
    return ic

def find_key_length(encrypted_text):
    # Try different key lengths and calculate IC for each
    max_length = min(20, len(encrypted_text))
    ic_values = []

    for key_length in range(1, max_length + 1):
        segments = [encrypted_text[i::key_length] for i in range(key_length)]
        avg_ic = sum(calculate_ic(segment) for segment in segments) / key_length
        ic_values.append((key_length, avg_ic))

    # Find the key length with the highest IC
    best_key_length, _ = max(ic_values, key=lambda x: x[1])
    return best_key_length

# Example usage:
encrypted_text = "Rkfojyhu amavq jw slwjfsvctsv!"
best_key_length = find_key_length(encrypted_text)
print("Best Key Length:", best_key_length)

# Now, let's try to find the key using common English words (a simple dictionary attack)
with open("english_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)

key = ""
for i in range(best_key_length):
    segment = encrypted_text[i::best_key_length]
    most_common_word = max(english_words, key=segment.count)
    key_char = chr(((ord(most_common_word) - ord('a')) % 26) + ord('a'))
    key += key_char

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted with Key:", key)
print("Decrypted Text:", decrypted_text)
