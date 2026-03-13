# src/recommender.py
from vector_search import search_movies
from ranking import rank_candidates
import pandas as pd
import numpy as np

def recommend(query, top_k=5):
    # Step 1: Get candidates from vector search
    candidates = search_movies(query, top_k=top_k*2)
    # Step 2: Rank candidates
    ranked = rank_candidates(candidates)
    # Step 3: Return top K
    return ranked.head(top_k)[['title', 'avg_rating', 'rating_count', 'similarity', 'score']]

if __name__ == "__main__":
    query = "Action and Adventure movies with Tom Cruise"
    results = recommend(query, top_k=5)
    print(results)
