import re
import string
import sys
import collections
import math
import functools
import cipher_and_decipher
import consts
# HELLO
# KEY
# Input

cipher_text = input("Ciphertext: ")
cipher_text = re.sub('[^a-zA-Z]+', '', cipher_text)
cipher_text = cipher_text.upper()

plain_text = input("Plaintext: ")
plain_text = re.sub('[^a-zA-Z]+', '', plain_text)
plain_text = plain_text.upper()

keyword =input("Keyword: ").upper()
key_size = cipher_text if cipher_text else plain_text

key = cipher_and_decipher.generate_key(key_size, keyword)


# Cipher and decipher
if sys.argv[1] == "cipher":
    print(f'Original: {plain_text}')
    print('=' * 30)

    if cipher_text and keyword:
        decripted = cipher_and_decipher.decipher(cipher_text, key)
    else:
        encripted = cipher_and_decipher.cipher(plain_text, key)
        decripted = cipher_and_decipher.decipher(encripted, key)
        
        print(f"Encripted: {encripted}")
        print('=' * 30)
    
    print(f"Key: {key}")
    print('=' * 30)
    print(f"Decripted: {decripted}")

else:
    # Attack

    def find_repeating_patterns(text, min_length=3):
        patterns = {} 
        for length in range(min_length, len(text)):
            for i in range(len(text) - length + 1):
                pattern = text[i:i+length]
                if pattern in patterns:
                    patterns[pattern].append(i)
                else:
                    patterns[pattern] = [i]

        repeating_patterns = {pattern: positions for pattern, positions in patterns.items() if len(positions) > 1}

        return repeating_patterns

    # Example usage:
    cipher_text = cipher_text
    repeating_patterns = find_repeating_patterns(cipher_text)
    print(f'Repeating Patterns = {repeating_patterns}')
    print('=' * 30)

    def identify_distance_between_repeats(repeating_patterns):
        distances = {}

        for pattern, positions in repeating_patterns.items():
            pattern_distances = []
            for i in range(len(positions) - 1):
                distance = positions[i + 1] - positions[i]
                pattern_distances.append(distance)
            distances[pattern] = pattern_distances

        return distances

    distance_between_repeats = identify_distance_between_repeats(repeating_patterns)
    print(f'Distance Between Repeats = {distance_between_repeats}')
    print('=' * 30)

    def calculate_gcd(numbers):
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required to calculate the GCD.")

        return functools.reduce(math.comb, numbers)

    distance_between_repeats_values_only = [item for row in distance_between_repeats.values() for item in row]
    gdc = calculate_gcd(distance_between_repeats_values_only)
    print(f'GDC = {gdc}')
    print('=' * 30)

    def calculate_index_of_coincidence(cipher_text: str):
        total_characters = len(cipher_text)

        # Initialize a dictionary to count the frequency of each letter
        letter_count = {}

        # Count the occurrences of each letter in the text
        for char in cipher_text:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

        # Calculate the Index of Coincidence
        ioc = 0.0
        for count in letter_count.values():
            ioc += (count * (count - 1)) / (total_characters * (total_characters - 1))

        return ioc

    # F

