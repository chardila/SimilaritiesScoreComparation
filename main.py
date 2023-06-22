import time

import CosineSimilarity
import DiceCoefficient
import Euclidean
import Hamming
import HashDifference
import Jaccard
import SecuenceMatcher


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

    print('Jaccard similarity:', jaccard_similarity_score)
    print("Time: ", end_time - start_time)

    size1 = len(set(strings1))
    size2 = len(set(strings2))

    start_time = time.time()
    dice_score = DiceCoefficient.dice_coefficient(strings1, strings2, size1, size2)
    end_time = time.time()

    print("Dice coefficient Similarity:", dice_score)
    print("Time: ", end_time - start_time)

    hash1 = Hamming.calculate_sha256_hash(strings1)
    hash2 = Hamming.calculate_sha256_hash(strings2)

    start_time = time.time()
    distance = Hamming.hamming_similarity(hash1, hash2)
    end_time = time.time()
    print("Hamming distance Similarity:", distance)
    print("Time: ", end_time - start_time)

    start_time = time.time()
    similarity = Euclidean.euclidean_similarity(strings1, strings2)
    end_time = time.time()
    print("Euclidean similarity:", similarity)
