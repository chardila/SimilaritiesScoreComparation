import time

import CosineSimilarity
import DiceCoefficient
import Euclidean
import Hamming
import HashDifference
import Jaccard
import SecuenceMatcher


def perform(fun, *args):

    start_time = time.time()
    similarity = fun(*args)
    end_time = time.time()

    dif_time = end_time - start_time

    print(fun.__name__, ":", similarity)
    print("time:", dif_time)

    return similarity, dif_time


if __name__ == '__main__':

    strings1 = ["example", "another", "string"]
    # strings2 = ["other", "example", "string"]
    strings2 = ["example", "another", "string"]

    best_similarity_score, best_time = perform(SecuenceMatcher.sequence_matcher_score, strings1, strings2)
    best_algorithm = "Sequence Matcher Similarity"

    similarity_score, exec_time = perform(CosineSimilarity.cosine_similarity_vectors, strings1, strings2)
    if best_time > exec_time:
        best_similarity_score = similarity_score
        best_time = exec_time
        best_algorithm = "Cosine Similarity"

    similarity_score, exec_time = perform(HashDifference.calculate_hash_difference_similarity, strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Hash Difference Similarity"

    similarity_score, exec_time = perform(Jaccard.jaccard_similarity, strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Jaccard Similarity"

    similarity_score, exec_time = perform(DiceCoefficient.dice_coefficient, strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Dice coefficient Similarity"

    similarity_score, exec_time = perform(Hamming.hamming_similarity, strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Hamming distance Similarity"

    similarity_score, exec_time = perform(Euclidean.euclidean_similarity, strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Hamming distance Similarity"

    print("Best Similarity Algorithm :", best_algorithm)
    print("Best Execution Time : ", best_time)
