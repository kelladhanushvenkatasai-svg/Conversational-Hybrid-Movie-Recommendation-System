import pandas as pd
import os
from sentence_transformers import SentenceTransformer
import numpy as np

processed_path = os.path.join("data", "processed_movies.csv")
movie_data = pd.read_csv(processed_path)

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(movie_data["text"].tolist(), show_progress_bar=True)


np.save(os.path.join("data", "movie_embeddings.npy"), embeddings)

print("Embeddings created and saved. Shape:", embeddings.shape)
