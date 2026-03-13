# Conversational Hybrid Movie Recommendation System

This project implements a **conversational hybrid movie recommender** that combines **content-based embeddings** and **collaborative filtering** to deliver personalized movie recommendations.

Users can query the system using **movie titles, genres, or natural language descriptions**, and receive **ranked movie suggestions** through a web interface connected to a **FastAPI backend**. The system uses **Python-based vector similarity search**, making it lightweight, efficient, and cross-platform.


# Problem Statement

Movie recommendation is challenging because of the **large volume of content and diverse user preferences**. Traditional recommendation systems often struggle to capture semantic similarity between movies, contextual relevance of user queries, and personalization based on user ratings.

This project addresses these limitations by combining **content-based embeddings to capture semantic similarity**, **collaborative filtering using user ratings**, and **natural language query parsing to support conversational movie search**. The goal is to provide accurate and meaningful recommendations even when users provide partial or descriptive queries.


# Features

- Conversational querying using **movie titles, genres, or descriptions**
- **Hybrid recommendation system** combining content similarity and collaborative filtering
- **Semantic search using embeddings**
- Interactive **web interface** using HTML, CSS, and JavaScript
- Modular architecture for easy **extension and maintenance**

---

# Tech Stack

## Backend
- Python 3.11+
- FastAPI
- Uvicorn

## Data & Machine Learning
- pandas
- NumPy
- scikit-learn
- sentence-transformers

## Frontend
- HTML
- CSS
- JavaScript

---

# Project Structure
conversational-movie-recommender/

├── src/ # Core ML pipeline and recommendation modules
│ ├── init.py # Makes src a Python package
│ ├── data_loader.py # Load movies and ratings datasets
│ ├── preprocess.py # Data preprocessing
│ ├── embeddings.py # Generate movie embeddings
│ ├── vector_search.py # Vector similarity search
│ ├── recommender.py # Hybrid recommendation logic
│ ├── ranking.py # Ranking functions
│ ├── query_parser.py # Parse user queries
│ └── pipeline.py # End-to-end recommendation pipeline
│
├── app.py # FastAPI application
│
├── static/ # Frontend interface
│ └── index.html
│
├── data/ # Input datasets
│ ├── movies.csv
│ ├── ratings.csv
│ └── processed_movies.csv
│
├── venv/ # Python virtual environment (ignored in Git)
│
├── requirements.txt # Project dependencies
└── README.md


# Installation

Clone the repository:

git clone https://github.com/kelladhanushvenkatasai-svg/Conversational-Hybrid-Movie-Recommendation-System

cd conversational-movie-recommender

Create and activate a virtual environment:

### Windows

python -m venv venv
venv\Scripts\activate

### macOS / Linux

python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

# Running the Application

Start the FastAPI server:

uvicorn app:app --reload

Then open the web interface in your browser.

# How to Use

1. Enter a **movie title**, **genre**, or **description**
2. Click **Submit**
3. The system will return a **ranked list of recommended movies**

# Future Improvements

- Integrate **large language models (LLMs)** for advanced semantic understanding
- Add **user authentication and personalized profiles**
- Store datasets in a **database for scalability**
- Incorporate **multi-modal embeddings** (posters, trailers, visual features)
- Extend the web interface with **chat-style conversational interactions**


# Author

**Dhanush Venkata Sai Kella**  
Master's in Information Technology  
California Lutheran University