import streamlit as st
import pandas as pd
import pickle
import requests
import time


movies_df = pickle.load(open('/Users/jagan/Desktop/scipy/projects/movies.pkl','rb'))
movie_titles = movies_df['title'].values
similarity = pickle.load(open('/Users/jagan/Desktop/scipy/projects/similarity.pkl','rb'))

TMDB_TOKEN = st.secrets["TMDB_TOKEN"]

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"
}


session = requests.Session()
session.headers.update(headers)

def fetch_poster(movie_id, max_retries=7):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    
    for attempt in range(max_retries):
        try:
            # Use session with longer timeout
            response = session.get(url, timeout=15)
            
            if response.status_code == 429:  # Rate limit hit
                wait_time = min((2 ** attempt) * 2, 30)  # Cap at 30 seconds
                time.sleep(wait_time)
                continue
                
            if response.status_code == 200:
                data = response.json()
                if 'poster_path' in data and data['poster_path']:
                    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
                else:
                    return None
            else:
                # Handle other HTTP errors
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                return None
                
        except (requests.exceptions.ConnectionError, 
                requests.exceptions.Timeout,
                ConnectionResetError) as e:
            # Handle connection errors with exponential backoff
            wait_time = min(2 ** attempt, 16)  # 1, 2, 4, 8, 16 seconds max
            if attempt < max_retries - 1:
                time.sleep(wait_time)
                continue
            else:
                return None
                
        except requests.exceptions.RequestException as e:
            # Handle other requests exceptions
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None
            
        except Exception as e:
            # Handle any other unexpected errors
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return None
    
    return None

def recommendation(movie):
    try:
        # Find the movie index
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get similarity distances
        distances = similarity[movie_index]
        
        # Get top 6 similar movies (reduced from 10 to minimize API calls)
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:7]
        
        recommended_movies = []
        recommended_movies_posters = []
        recommended_movie_ids = []
        
        for idx, i in enumerate(movies_list):
            movie_id = int(movies_df.iloc[i[0]].movie_id)
            movie_title = movies_df.iloc[i[0]]['title']
            
            recommended_movies.append(movie_title)
            recommended_movie_ids.append(movie_id)
            
            # Fetch poster with error handling
            poster = fetch_poster(movie_id)
            recommended_movies_posters.append(poster)
            
            # Batch poster fetching with smart delays
            if (idx + 1) % 3 == 0:  # Every 3rd request
                if idx < len(movies_list) - 1:  # Don't delay after the last request
                    time.sleep(5.0)  # Longer pause every 3 requests
            else:
                if idx < len(movies_list) - 1:  # Don't delay after the last request
                    time.sleep(2.0)  # 2 seconds between requests
        
        return recommended_movies, recommended_movies_posters, recommended_movie_ids
        
    except IndexError:
        st.error("Movie not found in database. Please select a different movie.")
        return [], [], []
    except Exception as e:
        st.error(f"Error in recommendation: {str(e)}")
        return [], [], []

@st.cache_data(show_spinner=False)
def get_cached_recommendations(movie_name):
    return recommendation(movie_name)

# Initialize session state
if 'loading' not in st.session_state:
    st.session_state.loading = False

# Streamlit UI
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    "Choose a movie:",
    movie_titles
)

if st.button('Get Recommendations', disabled=st.session_state.loading):
    if not selected_movie_name:
        st.warning("Please select a movie first!")
    else:
        st.session_state.loading = True
        
        try:
            with st.spinner('Getting recommendations...'):
                rec, posters, movie_num = get_cached_recommendations(selected_movie_name)
            
            st.session_state.loading = False
            
            if rec:
                # Display in rows of 3 for better layout with 6 movies
                cols = st.columns(3)
                for idx in range(min(3, len(rec))):
                    with cols[idx]:
                        st.markdown(f"**{rec[idx]}**")
                        if posters[idx]:
                            st.image(posters[idx], width=200)
                        else:
                            st.image("https://via.placeholder.com/500x750?text=No+Poster", width=200)
                
                # Second row if more than 3 recommendations
                if len(rec) > 3:
                    cols2 = st.columns(3)
                    for idx in range(3, min(6, len(rec))):
                        with cols2[idx-3]:
                            st.markdown(f"**{rec[idx]}**")
                            if posters[idx]:
                                st.image(posters[idx], width=200)
                            else:
                                st.image("https://via.placeholder.com/500x750?text=No+Poster", width=200)
                
        except Exception as e:
            st.session_state.loading = False