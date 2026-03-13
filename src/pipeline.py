# src/pipeline.py
import pandas as pd
from .vector_search import search_movies
from .ranking import rank_candidates
from .parsing import parse_query

movie_data = pd.read_csv("data/processed_movies.csv")

def run_pipeline(query, top_k=5):
    parsed = parse_query(query)
    keywords = parsed['keywords']
    genres = parsed['genres']
    min_rating = parsed['min_rating']

    # Search
    candidates = search_movies(keywords, top_k=top_k*2)

    # Filter genres
    if genres:
        candidates = candidates[candidates['genres'].apply(lambda x: any(g in x for g in genres))]

    #  Filter by rating
    if min_rating > 0:
        candidates = candidates[candidates['avg_rating'] >= min_rating]

    #  Rank
    ranked = rank_candidates(candidates)

    #  Return top K
    return ranked.head(top_k)[['title', 'avg_rating', 'rating_count', 'similarity', 'score']]

if __name__ == "__main__":
    query = input("Enter your movie query: ")
    results = run_pipeline(query, top_k=5)
    print(results)
