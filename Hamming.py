import hashlib


def hex_to_binary(hex_hash):
    binary_hash = bin(int(hex_hash, 16))[2:].zfill(len(hex_hash) * 4)
    return binary_hash



def calculate_sha256_hash(data):
    combined_string = '|'.join(data)
    sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()
    return sha256_hash

def hamming_similarity(s1, s2):

    hash1 = calculate_sha256_hash(s1)
    hash2 = calculate_sha256_hash(s2)
    if len(hash1) != len(hash2):
        raise ValueError("Hashes must have the same length")

    binary_hash1 = hex_to_binary(hash1)
    binary_hash2 = hex_to_binary(hash2)

    total_bits = len(binary_hash1)
    differing_bits = sum(bit1 != bit2 for bit1, bit2 in zip(binary_hash1, binary_hash2))

    hamming_similarity_result = 1 - (differing_bits / total_bits)

    return hamming_similarity_result
