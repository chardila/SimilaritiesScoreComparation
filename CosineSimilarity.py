from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity_vectors(vectors1, vectors2):
    # Combine the strings from both vectors into a single list
    combined_strings = [' '.join(vectors1), ' '.join(vectors2)]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the combined strings into TF-IDF vectors
    vectors = vectorizer.fit_transform(combined_strings)

    # Calculate the cosine similarity matrix
    similarity_matrix = cosine_similarity(vectors)

    # Extract the cosine similarity score for the pair of interest
    similarity_score_result = similarity_matrix[0, 1]

    return similarity_score_result