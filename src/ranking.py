# src/ranking.py
import numpy as np

def rank_candidates(candidates):
    """
    Hybrid ranking using similarity, avg_rating, and rating_count
    """
    candidates['score'] = (
        0.5 * candidates['similarity'] +
        0.3 * (candidates['avg_rating'] / 5) +
        0.2 * np.log1p(candidates['rating_count'])
    )
    return candidates.sort_values('score', ascending=False)
