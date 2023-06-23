# imports for calculate_hash_difference_similarity method
import hashlib
import MeasureExecTimes


def calculate_md5hash(features):
    # Combine the elements of the features list into a single string
    combined_string = '|'.join(features)

    # Calculate the MD5 hash of the combined string
    md5_hash = hashlib.md5(combined_string.encode()).hexdigest()
    return md5_hash

@MeasureExecTimes.measure_execution_time
def get_hash_difference_similarity_score(string1, string2):
    pid1 = calculate_md5hash(string1)
    pid2 = calculate_md5hash(string2)

    # Convert the hexadecimal representations to binary strings
    binary_id1 = bin(int(pid1, 16))[2:].zfill(len(pid1) * 4)
    binary_id2 = bin(int(pid2, 16))[2:].zfill(len(pid2) * 4)

    # Count the matching digits
    rta_similarity = sum(bit1 == bit2 for bit1, bit2 in zip(binary_id1, binary_id2))

    # Normalize the similarity score between 0 and 1
    max_similarity = max(len(binary_id1), len(binary_id2))
    hash_difference = rta_similarity / max_similarity
    return hash_difference
