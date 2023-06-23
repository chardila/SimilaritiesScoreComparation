import time

import CosineSimilarity
import DiceCoefficient
import Euclidean
import Hamming
import HashDifference
import Jaccard
import SecuenceMatcher


def perform(fun, *args):
    # Measure the start time of the function execution
    start_time = time.time()

    # Call the provided function (fun) with the given arguments (args)
    similarity = fun(*args)

    # Measure the end time of the function execution
    end_time = time.time()

    # Calculate the time difference
    dif_time = end_time - start_time

    # Print the function name, similarity result, and execution time
    print(fun.__name__, ":", similarity)
    print("time:", dif_time)

    # Return the similarity result and execution time as a tuple
    return similarity, dif_time


if __name__ == '__main__':
    # Entry point of the program when it is run as the main script

    # Define two lists of strings
    strings1 = ["example", "another", "string"]
    strings2 = ["other", "example", "string"]
    # strings2 = ["example", "another", "string"]

    # Measure and compare the performance of different similarity algorithms

    # Perform sequence matching similarity calculation
    best_similarity_score, best_time = SecuenceMatcher.get_sequence_matcher_score(strings1, strings2)
    best_algorithm = "Sequence Matcher Similarity"

    # Perform cosine similarity calculation
    similarity_score, exec_time = CosineSimilarity.get_cosine_similarity_score(strings1, strings2)
    if best_time > exec_time:
        best_similarity_score = similarity_score
        best_time = exec_time
        best_algorithm = "Cosine Similarity"

    # Perform hash difference similarity calculation
    similarity_score, exec_time = HashDifference.get_hash_difference_similarity_score(strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Hash Difference Similarity"

    # Perform Jaccard similarity calculation
    similarity_score, exec_time = Jaccard.get_jaccard_similarity_score(strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Jaccard Similarity"

    # Perform Dice coefficient similarity calculation
    similarity_score, exec_time = DiceCoefficient.get_dice_coefficient_score(strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Dice coefficient Similarity"

    # Perform Hamming similarity calculation
    similarity_score, exec_time = Hamming.get_hamming_similarity_score(strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Hamming distance Similarity"

    # Perform Euclidean similarity calculation
    similarity_score, exec_time = Euclidean.get_euclidean_similarity_score(strings1, strings2)
    if best_time > exec_time:
        best_time = exec_time
        best_algorithm = "Euclidean Similarity"

    # Print the best similarity algorithm and execution time
    print("Best Similarity Algorithm:", best_algorithm)
    print("Best Execution Time:", best_time)
