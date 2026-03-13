import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load preprocessed movie data
movies_path = os.path.join("data", "processed_movies.csv")
movie_data = pd.read_csv(movies_path)

# Step 1: Create TF-IDF embeddings
vectorizer = TfidfVectorizer(max_features=5000)  # adjust size if needed
movie_vectors = vectorizer.fit_transform(movie_data["text"])

# Step 2: Function to search top K movies
def search_movies(query, top_k=5):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, movie_vectors).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]
    results = movie_data.iloc[top_indices].copy()
    results["similarity"] = similarities[top_indices]
    return results

# Example usage
if __name__ == "__main__":
    query = "Action and Adventure movies with Tom Cruise"
    top_movies = search_movies(query, top_k=5)
    print(top_movies[["title", "avg_rating", "rating_count", "similarity"]])
