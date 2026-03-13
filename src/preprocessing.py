import pandas as pd
import os

movie_path = os.path.join('data','movies.csv')
rating_path = os.path.join('data', 'ratings.csv')

movies = pd.read_csv(movie_path)
ratings = pd.read_csv(rating_path)

movie_stats = ratings.groupby("movieId").agg({
    "rating": ["mean", "count"]
})

movie_stats.columns = ["avg_rating", "rating_count"]
movie_stats = movie_stats.reset_index()

movie_data = movies.merge(movie_stats, on= 'movieId', how = 'left')

movie_data["avg_rating"].fillna(0, inplace=True)
movie_data["rating_count"].fillna(0, inplace=True)

movie_data["text"] = movie_data["title"] + " " + movie_data["genres"]

movie_data.to_csv(os.path.join("data", "processed_movies.csv"), index=False)

print("Preprocessing done. Sample data:")
print(movie_data.info())