# Content-Based Movie Recommendation System

**Live Demo**  
Try the live application here: [https://harich.streamlit.app/](https://harich.streamlit.app/)

---

## Project Overview

This project is an end-to-end content-based movie recommendation system that suggests movies based on their plot, genre, keywords, cast, and crew. It leverages advanced Natural Language Processing (NLP) techniques to understand the semantic context of movies for intelligent recommendations.

- **Core Function:** Recommends movies by analyzing and comparing their content profiles.
- **Key Technology:** Uses **spaCy's** powerful NLP model to convert movie information into rich semantic vectors for meaningful similarity comparison.
- **API Integration:** Dynamically fetches movie posters from The Movie Database (TMDB) API to create an engaging UI.
- **Deployment:** Packaged as a user-friendly Streamlit web application showcasing both data science and deployment skills.

---

## Tech Stack

- Python  
- spaCy (en_core_web_lg model)  
- Scikit-learn  
- Pandas  
- NumPy  
- Streamlit  
- Jupyter Notebook  

---

## Methodology

1. **Feature Engineering:**  
   Extracted key attributes such as genres, keywords, overview, cast, and director from the TMDB dataset. These attributes were combined into a single "tag" representing each movie’s content.

2. **Semantic Vectorization:**  
   Instead of basic keyword matching, spaCy’s `en_core_web_lg` model was used to transform each movie's tag into a 300-dimensional semantic vector, capturing deeper contextual meaning.

3. **Similarity Calculation:**  
   Used scikit-learn's `cosine_similarity` on these vectors to measure semantic closeness between movies. The system recommends movies with the highest similarity scores.

---

## Performance Note

Due to TMDB API rate limitations, fetching movie posters in real-time can introduce longer loading times. The application includes intentional delays and error handling to respect these API limits and ensure stable performance.

---

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```
2. Install dependencies:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```


## Folder Structure (Example)

```perl

movie-recommendation-system/
│
├── app.py                   # Main Streamlit app file
├── movies.pkl               # Pickled dataframe with movie data
├── similarity.pkl           # Pickled similarity matrix
├── requirements.txt         # Python dependencies
├── README.md
└── utils.py                 # (Optional) utility functions for API calls, etc.
```


### Installing spaCy and the Language Model

Before running the app, make sure to install spaCy and download the required English language model:

```bash
pip install spacy
python -m spacy download en_core_web_lg




