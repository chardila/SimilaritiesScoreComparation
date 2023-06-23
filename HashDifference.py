# imports for calculate_hash_difference_similarity method
import hashlib
import HashDifference


def calculate_identifier(features):
    combined_string = '|'.join(features)
    md5_hash = hashlib.md5(combined_string.encode()).hexdigest()
    return md5_hash


def calculate_hash_difference_similarity(string1, string2):

    pid1 = HashDifference.calculate_identifier(string1)
    pid2 = HashDifference.calculate_identifier(string1)

    # Convert the hexadecimal representations to binary strings
    binary_id1 = bin(int(pid1, 16))[2:].zfill(len(pid1) * 4)
    binary_id2 = bin(int(pid2, 16))[2:].zfill(len(pid2) * 4)

    # Count the matching digits
    rta_similarity = sum(bit1 == bit2 for bit1, bit2 in zip(binary_id1, binary_id2))

    # Normalize the similarity score between 0 and 1
    max_similarity = max(len(binary_id1), len(binary_id2))
    hash_difference = rta_similarity / max_similarity
    return hash_difference
