
import numpy as np


def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0

    similarity = dot_product / (magnitude_a * magnitude_b)

    return float(similarity)


def retrieve_chunks(query_embedding, embeddings, chunks, top_k=3):
    similarities = []

    for index, embedding in enumerate(embeddings):
        score = cosine_similarity(query_embedding, embedding)

        similarities.append((index, score))

    # Sort by similarity score (highest first)
    similarities.sort(key=lambda item: item[1], reverse=True)

    # Select the top matching chunks
    top_chunks = []

    for index, score in similarities[:top_k]:
        top_chunks.append({
            "chunk": chunks[index],
            "score": score
        })

    return top_chunks
