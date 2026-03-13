import pandas as pd
import os

movie_path = os.path.join('data','movies.csv')
rating_path = os.path.join('data', 'ratings.csv')

movies = pd.read_csv(movie_path)
ratings = pd.read_csv(rating_path)

print(movies.head())
print(ratings.head())