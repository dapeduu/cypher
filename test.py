import re
import string
import sys
import collections
import math
import functools
import cipher_and_decipher
import consts
# Input

text = """rvgllakieg tye tirtucatzoe.  whvnvvei i
    winu mpsecf xronieg giid abfuk thv mfuty; wyenvvvr ik ij a drmg,
    drzzqly eomemsei in dy jouc; wyenvvvr i wied mpsvlf znmollnkarzlp
    palszng seworv cfffzn narvhfusvs, rnd srzngznx up khv rerr ff emeiy
    flnvrac i deek; aed ejpvcirlcy wyeeevvr dy hppfs gvt jucy ae upgei
    haed ff mv, tyat zt ieqliies r skroeg dorrl grieczplv tf prvvvnt de
    wrod dvliseiatvlp stvpginx ieto khv stievt, aed detyouicrlcy keotkieg
    geoglv's hrtj ofw--tyen, z atcolnk it yixh tzmv to xek to jer as jofn
    aj i tan.  khzs ij mp susskitltv foi pzstfl rnd sacl.  wzty a
    pyicosfpyicrl wlolrzsh tako tyrfws yidsecf lpoe hzs snoid; i huzetcy
    kakv tf thv syip.  khvre zs eotyieg slrgrijieg ie tyis.  zf khep blt
    keen it, rldosk acl mvn zn tyezr dvgiee, jode tzmv or ftyer, thvrijh
    merp nvarcy khe jade fvecinxs kowrrus tye fcern nity mv."""
text = re.sub('[^a-zA-Z]+', '', text)
text = text.upper()
keyword = "arara".upper()
key = cipher_and_decipher.generate_key(text, keyword)


# Cipher and decipher

if sys.argv[0] == "cipher":
    encripted = cipher_and_decipher.cipher(text, key)
    decripted = cipher_and_decipher.decipher(text, key)

    print(f'Original: {text}')
    print('=' * 30)
    print(f"Encripted: {encripted}")
    print('=' * 30)
    print(f"Key: {key}")
    print('=' * 30)
    print(f"Decripted: {decripted}")

    sys.exit(0)


# Attack

def find_repeating_patterns(text, min_length=3):
    patterns = {}  # Dictionary to store patterns and their positions

    for length in range(min_length, len(text)):
        for i in range(len(text) - length + 1):
            pattern = text[i:i+length]
            if pattern in patterns:
                patterns[pattern].append(i)
            else:
                patterns[pattern] = [i]

    # Filter out patterns that only appear once
    repeating_patterns = {pattern: positions for pattern, positions in patterns.items() if len(positions) > 1}

    return repeating_patterns

# Example usage:
cipher_text = text
repeating_patterns = find_repeating_patterns(cipher_text)
print(f'Repeating Patterns = {repeating_patterns}')
print('=' * 30)

def identify_distance_between_repeats(repeating_patterns):
    distances = {}  # Dictionary to store distances between repeats for each pattern

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
    
    return functools.reduce(math.gcd, numbers)

distance_between_repeats_values_only = [item for row in distance_between_repeats.values() for item in row]
gdc = 5 #calculate_gcd(distance_between_repeats_values_only)
print(f'GDC = {gdc}')
print('=' * 30)

def divide_ciphertext_into_groups(ciphertext, key_length):
    groups = [''] * key_length  # Create empty strings for each group

    for i, char in enumerate(ciphertext):
        group_index = i % key_length
        groups[group_index] += char

    return groups

cipher_text_divided_by_key_length = divide_ciphertext_into_groups(cipher_text, gdc)
print(f'Cipher Text Divided By Key Length = {cipher_text_divided_by_key_length}')
print('=' * 30)

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