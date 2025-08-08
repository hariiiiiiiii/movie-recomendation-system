# Content-Based Movie Recommendation System

### 🔴 Live Demo
**You can try the live application here:** [https://your-streamlit-app-url.streamlit.app](https://your-streamlit-app-url.streamlit.app)
*(Note: Replace with your actual URL after deployment)*

---

### Project Overview

This project is an end-to-end movie recommendation system that suggests films based on their content. The model was developed using Natural Language Processing (NLP) to understand the semantic context of movies, and the final application was deployed as an interactive web app with Streamlit.

* **Core Function:** Recommends movies by analyzing plot, genre, keywords, cast, and crew.
* **Key Technology:** Leverages **`spaCy`'s** advanced NLP capabilities to convert movie data into meaningful vectors, enabling intelligent, context-aware recommendations.
* **API Integration:** Fetches movie posters from The Movie Database (TMDB) API in real-time to create a dynamic and visually engaging user interface.
* **Deployment:** The entire system is packaged into a user-friendly Streamlit application, demonstrating skills in both data science and application deployment.

### Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)

---

### Methodology

The recommendation engine was built using the following steps:

1.  **Feature Engineering:** Key data points from the TMDB dataset (genres, keywords, overview, cast, director) were extracted and merged into a single "tag" for each movie. This creates a comprehensive content profile for every film.

2.  **Semantic Vectorization:** Instead of simple keyword matching, `spaCy`'s `en_core_web_lg` model was used to transform each movie's tag into a sophisticated 300-dimensional vector. These vectors capture the semantic meaning of the movie's content.

3.  **Similarity Calculation:** `scikit-learn`'s `cosine_similarity` was applied to the vector matrix to calculate the contextual closeness between every pair of movies. Movies with the highest similarity scores are then recommended.

### Performance Note

To ensure the application is a stable and responsible consumer of the TMDB API, intentional delays and error-handling logic have been implemented to manage API rate limits. This may result in a brief loading period as movie posters are fetched in real-time.

---

### Run Locally

To set up and run this project on your local machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/movie-recommendation-system.git](https://github.com/your-username/movie-recommendation-system.git)
cd movie-recommendation-system
