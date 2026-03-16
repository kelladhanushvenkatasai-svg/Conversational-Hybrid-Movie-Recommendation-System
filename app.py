# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.pipeline import run_pipeline  # your pipeline.py
from fastapi.responses import FileResponse

app = FastAPI(title="Movie Recommender API")

# Serve HTML + JS from static folder
app.mount("/static", StaticFiles(directory="static"), name="static")
# CORS for front-end JS calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class MovieQuery(BaseModel):
    query: str
    top_k: int = 5


@app.get("/")
def home():
    return FileResponse("static/index.html")

# API endpoint
@app.post("/recommend")
def recommend_movies(movie_query: MovieQuery):
    results = run_pipeline(movie_query.query, top_k=movie_query.top_k)
    return results.to_dict(orient="records")
