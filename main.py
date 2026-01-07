from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import pandas as pd
import requests
import os
import uvicorn
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
app = FastAPI()

# Setup Folders
for folder in ["static", "templates", "models"]:
    if not os.path.exists(folder): os.makedirs(folder)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load Data
try:
    with open("models/df.pkl", "rb") as f:
        movies_df = pickle.load(f)
    with open("models/indices.pkl", "rb") as f:
        indices = pickle.load(f)
    TITLE_COL = 'title' if 'title' in movies_df.columns else movies_df.columns[0]
except Exception as e:
    print(f"Error: {e}")
    movies_df = pd.DataFrame(columns=['title'])
    TITLE_COL = 'title'

def fetch_poster(movie_title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get('results') and data['results'][0].get('poster_path'):
            return f"https://image.tmdb.org/t/p/w500{data['results'][0]['poster_path']}"
        return "https://via.placeholder.com/500x750?text=No+Poster"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

def get_recommendations(title, num_rec):
    try:
        with open("models/tfidf_matrix.pkl", "rb") as f:
            tfidf_matrix = pickle.load(f)
        idx = indices[title]
        sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
        sim_indices = sim_scores.argsort()[:-(num_rec + 2):-1]
        results = []
        for i in sim_indices:
            m_title = movies_df.iloc[i][TITLE_COL]
            if m_title != title:
                results.append({"title": m_title, "poster": fetch_poster(m_title)})
        del tfidf_matrix
        return results[:num_rec]
    except:
        return []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    movie_list = sorted(movies_df[TITLE_COL].astype(str).unique().tolist())
    return templates.TemplateResponse("index.html", {"request": request, "movies": movie_list})

@app.post("/recommend", response_class=HTMLResponse)
async def recommend(request: Request, movie_name: str = Form(...), num_movies: int = Form(...)):
    recommendations = get_recommendations(movie_name, num_movies)
    movie_list = sorted(movies_df[TITLE_COL].astype(str).unique().tolist())
    return templates.TemplateResponse("index.html", {
        "request": request, "movies": movie_list, 
        "recommendations": recommendations, "selected_movie": movie_name,
        "current_num": num_movies
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8089)