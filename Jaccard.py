import MeasureExecTimes

@MeasureExecTimes.measure_execution_time
def get_jaccard_similarity_score(list1, list2):
    # Convert the input lists into sets
    set1 = set(list1)
    set2 = set(list2)

    # Calculate the intersection and union of the two sets
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # Calculate the Jaccard similarity score as the ratio of the intersection to the union
    jaccard_similarity_score = len(intersection) / len(union)

    return jaccard_similarity_score
