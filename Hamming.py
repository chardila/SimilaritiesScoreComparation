def hex_to_binary(hex_hash):
    binary_hash = bin(int(hex_hash, 16))[2:].zfill(len(hex_hash) * 4)
    return binary_hash


def hamming_similarity(ohash1, ohash2):
    if len(ohash1) != len(ohash2):
        raise ValueError("Hashes must have the same length")

    binary_hash1 = hex_to_binary(ohash1)
    binary_hash2 = hex_to_binary(ohash2)

    total_bits = len(binary_hash1)
    differing_bits = sum(bit1 != bit2 for bit1, bit2 in zip(binary_hash1, binary_hash2))

    hamming_similarity_result = 1 - (differing_bits / total_bits)

    return hamming_similarity_result
