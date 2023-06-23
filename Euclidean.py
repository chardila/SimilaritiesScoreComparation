import numpy as np
import MeasureExecTimes

def generate_vector(lst, vocabulary):
    vector = np.zeros(len(vocabulary))
    for word in lst:
        if word in vocabulary:
            vector[vocabulary.index(word)] = 1
    return vector

@MeasureExecTimes.measure_execution_time
def get_euclidean_similarity_score(list1, list2):
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
