def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union)