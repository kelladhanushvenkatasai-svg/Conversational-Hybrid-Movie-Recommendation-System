# src/query_parser.py
import re

def parse_query(query):
    """
    Extract genres, min_rating, and keywords
    """
    genres = []
    min_rating = 0
    keywords = query

    match = re.search(r"rated above (\d(?:\.\d)?)", query)
    if match:
        min_rating = float(match.group(1))

    possible_genres = ['Action', 'Adventure', 'Comedy', 'Drama', 'Romance', 'Sci-Fi', 'Horror']
    for g in possible_genres:
        if g.lower() in query.lower():
            genres.append(g)

    return {"genres": genres, "min_rating": min_rating, "keywords": keywords}
