from collections import Counter
import re
from cipher_and_decipher import decrypt

def calculate_index_of_coincidence(text):
    text = text.lower()  # Convert text to lowercase for case insensitivity
    text = re.sub(r'[^a-zA-Z]', '', text) # Only characters from a to z
    total_characters = len(text)

    # Initialize a dictionary to count the frequency of each letter
    letter_count = {}

    # Count the occurrences of each letter in the text
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Calculate the Index of Coincidence
    ioc = 0.0
    for count in letter_count.values():
        ioc += (count * (count - 1)) / (total_characters * (total_characters - 1))

    return ioc

# Example usage:
text = """
To be, or not to be, that is the question—
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them?
William Shakespeare - Hamlet
"""
ioc = calculate_index_of_coincidence(text)
print("Index of Coincidence:", ioc)
