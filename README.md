# MOVIE-RECOMMENDATION-SYSTEM---NLP-PROJECT

CineMatch AI: The "Movie DNA" Engine
Architected by Gaurav Singh
"Streaming services don't just sell movies; they sell the next movie. CineMatch AI doesn't guess—it analyzes the mathematical DNA of plotlines to predict user obsession."

App link: https://cinematch-by-gaurav-singh.onrender.com

🧠 The Project: From Raw Data to Intelligence
This project is not just a recommendation engine; it is a full-stack Data Science application designed to solve the "Cold Start Problem" in recommendation systems. Unlike collaborative filtering (which needs user history), CineMatch AI uses Content-Based Filtering to analyze the semantic meaning of movie tags, genres, and overviews.

We built this system from scratch, moving from raw CSV data analysis to a deployed, production-ready web application with a "Netflix-grade" UI.

⚙️ How It Works: The "Vector Space" Logic
Data Ingestion: Merged and cleaned the TMDB 5000 Movies Dataset, processing over 4,800 films.

Tag Engineering: Created a "soup" of metadata by combining Genres, Keywords, Cast, and Director into a single semantic string for each movie.

Vectorization (TF-IDF): Converted text into numerical vectors. This transformed every movie into a coordinate in a multi-dimensional space.

Cosine Similarity: The engine calculates the angular distance between vectors. The smaller the angle, the closer the "DNA" match between two movies.

🛠️ Tech Stack & Tools
Core Logic: Python, Pandas, NumPy, Scikit-Learn (Cosine Similarity).

API Framework: FastAPI (High-performance async backend).

Frontend: HTML5, CSS3 (Netflix-inspired Dark Mode), Jinja2 Templating.

Deployment: Render Cloud Hosting (CI/CD Pipeline via GitHub).

Version Control: Git & GitHub Desktop.

📉 Dataset & Scope
Source: TMDB 5000 Movie Dataset.

Volume: ~5,000 Movies processed.

Features Used: movie_id, title, overview, genres, keywords, cast, crew.

Time to Market: 4 Weeks of intensive iterative development, debugging, and UI refinement.

🚧 Architectural Challenges & Solutions
This project pushed the limits of free-tier cloud computing. Here is how we solved the major hurdles:

1. The "Memory Bottleneck" (Pickle Files)
Challenge: The vectorized model (tfidf_matrix.pkl) was massive. Loading it crashed standard local servers and exceeded GitHub's initial upload limits.

Solution: Optimized data types to reduce memory footprint and utilized Git LFS (Large File Storage) protocols for version control.

2. Deployment Pathing Hell
Challenge: Moving from a Windows Localhost environment to a Linux Cloud Server (Render) broke all relative file paths, causing Jinja2 Template Not Found errors.

Solution: Rewrote the backend to use dynamic, OS-agnostic pathing (os.path.dirname) and restructured the repository for root-level access, ensuring seamless cloud builds.

3. The "Cold Start" Latency
Challenge: Large AI models take time to load into RAM, causing slow startup times on the web.

Solution: Implemented efficient caching strategies and lightweight API endpoints to ensure the UI loads instantly while the model wakes up in the background.

🌍 Real-World Business Impact (MBA Perspective)
In the streaming economy, Retention is King.

Churn Reduction: By accurately predicting what a user wants to see next, platforms reduce the likelihood of subscription cancellation.

Long-Tail Discovery: This engine exposes users to lesser-known movies that mathematically match their interests, maximizing the ROI of the platform's content library.

Scalability: The content-based approach means this system works immediately for new users without needing months of historical watch data.

🚀 How to Run Locally
Want to inspect the "DNA" yourself?

Clone the Repo:

Bash

git clone https://github.com/gaurav280303/MOVIE-RECOMMENDATION-SYSTEM.git
Install Dependencies:

Bash

pip install -r requirements.txt
Ignite the Engine:

Bash

python main.py
Access UI: Open http://127.0.0.1:8000 in your browser.

Architected with 💻 and ☕ by Gaurav Singh.
