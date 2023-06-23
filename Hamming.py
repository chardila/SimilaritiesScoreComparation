import hashlib
import MeasureExecTimes


def hex_to_binary(hex_hash):
    # Convert hexadecimal hash to binary representation
    binary_hash = bin(int(hex_hash, 16))[2:].zfill(len(hex_hash) * 4)
    return binary_hash


def calculate_sha256_hash(data):
    # Combine the elements of the data list into a single string
    combined_string = '|'.join(data)

    # Calculate the SHA-256 hash of the combined string
    sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()
    return sha256_hash

@MeasureExecTimes.add_logging
def get_hamming_similarity_score(s1, s2):
    # Calculate SHA-256 hashes for the input strings
    hash1 = calculate_sha256_hash(s1)
    hash2 = calculate_sha256_hash(s2)

    # Check if the hashes have the same length
    if len(hash1) != len(hash2):
        raise ValueError("Hashes must have the same length")

    # Convert the hexadecimal hashes to binary representation
    binary_hash1 = hex_to_binary(hash1)
    binary_hash2 = hex_to_binary(hash2)

    # Calculate the Hamming similarity score
    total_bits = len(binary_hash1)
    differing_bits = sum(bit1 != bit2 for bit1, bit2 in zip(binary_hash1, binary_hash2))
    hamming_similarity_result = 1 - (differing_bits / total_bits)

    return hamming_similarity_result
