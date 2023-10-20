import re
from collections import Counter

def find_repeated_groups(text: str):
    def find_matches(text, search_string):
        return [m.start() for m in re.finditer(search_string, text)]

    MIN_REPETITIONS = 2 if len(text) < 200 else 3
    MIN_GROUP_LENGTH = 3 if len(text) < 200 else 5
    repeated_groups = {}

    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            search_string = text[i:j]
            matches_index = find_matches(text, search_string)

            if len(matches_index) >= MIN_REPETITIONS:
                repeated_groups[search_string] = matches_index
            elif search_string in repeated_groups and len(search_string) >= MIN_GROUP_LENGTH:
                break

    return repeated_groups

def find_distances(repeated_groups):
    matches_index = repeated_groups.values()
    distances = [b - a for indexes in matches_index for a, b in zip(indexes, indexes[1:])]
    return distances

def find_divisors(number):
    return [i for i in range(2, number + 1) if number % i == 0]

def find_most_common_divisors(distances):
    divisor_counts = Counter()
    for distance in distances:
        divisor_counts.update(find_divisors(distance))

    most_common_divisors = divisor_counts.most_common(3)
    return most_common_divisors

def find_key_length(cipher_text: str):
    repeated_groups = find_repeated_groups(cipher_text)
    distances = find_distances(repeated_groups)
    most_common_divisors = find_most_common_divisors(distances)

    if most_common_divisors:
        key_length, _count = max(most_common_divisors, key=lambda x: (x[1], x[0]))
        return key_length
