import hashlib
import time

# imports for Euclidean similarity
import numpy as np

import CosineSimilarity
import HashDifference
import SecuenceMatcher
import Jaccard
import DiceCoefficient
import Hamming


def calculate_sha256_hash(data):
    combined_string = '|'.join(data)
    sha256_hash = hashlib.sha256(combined_string.encode()).hexdigest()
    return sha256_hash





def euclidean_similarity(list1, list2):
    # Create a vocabulary of unique words
    vocabulary = list(set(list1 + list2))

    # Generate one-hot encoded vectors for each list
    vector1 = generate_vector(list1, vocabulary)
    vector2 = generate_vector(list2, vocabulary)

    # Calculate the Euclidean distance
    euclidean_distance = np.linalg.norm(vector1 - vector2)

    # Calculate the similarity score
    max_distance = np.sqrt(len(vocabulary))
    euclidean_similarity_result = 1 - (euclidean_distance / max_distance)

    return euclidean_similarity_result


def generate_vector(lst, vocabulary):
    vector = np.zeros(len(vocabulary))
    for word in lst:
        if word in vocabulary:
            vector[vocabulary.index(word)] = 1
    return vector


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    strings1 = ["example", "another", "string"]
    strings2 = ["other", "example", "string"]
    # strings2 = ["example", "another", "string"]

    start_time = time.time()
    similarity = SecuenceMatcher.sequence_matcher_score(strings1, strings2)
    end_time = time.time()

    print('Sequence Matcher Similarity:', similarity)
    print("Time: ", end_time - start_time)

    start_time = time.time()
    similarity_score = CosineSimilarity.cosine_similarity_vectors(strings1, strings2)
    end_time = time.time()

    print('Cosine Similarity:', similarity_score)
    print("Time: ", end_time - start_time)

    id1 = HashDifference.calculate_identifier(strings1)
    id2 = HashDifference.calculate_identifier(strings2)

    start_time = time.time()
    hash_difference_similarity = HashDifference.calculate_hash_difference_similarity(id1, id2)
    end_time = time.time()

    print("Hash Difference Similarity:", hash_difference_similarity)
    print("Time: ", end_time - start_time)

    start_time = time.time()
    jaccard_similarity_score = Jaccard.jaccard_similarity(strings1, strings2)
    end_time = time.time()

    print('Jaccard.py similarity:', jaccard_similarity_score)
    print("Time: ", end_time - start_time)

    size1 = len(set(strings1))
    size2 = len(set(strings2))

    start_time = time.time()
    dice_score = DiceCoefficient.dice_coefficient(strings1, strings2, size1, size2)
    end_time = time.time()

    print("Dice coefficient Similarity:", dice_score)
    print("Time: ", end_time - start_time)

    hash1 = calculate_sha256_hash(strings1)
    hash2 = calculate_sha256_hash(strings2)

    start_time = time.time()
    distance = Hamming.hamming_similarity(hash1, hash2)
    end_time = time.time()
    print("Hamming.py distance Similarity:", distance)
    print("Time: ", end_time - start_time)

    start_time = time.time()
    similarity = euclidean_similarity(strings1, strings2)
    end_time = time.time()
    print("Euclidean similarity:", similarity)
