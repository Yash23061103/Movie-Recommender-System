import streamlit as st
import pickle
import pandas as pd
import requests

# --- 1. CONFIGURATION & STYLING ---
# Sets the browser tab title and expands the layout to full screen
st.set_page_config(page_title="Movie Recommender", page_icon="🍿", layout="wide")

# Custom CSS for the dark cinematic theme
custom_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    background-image: radial-gradient(circle at top, #3b0000 0%, #0E1117 80%);
}
h1 { color: #E50914; text-align: center; font-weight: 800; margin-bottom: 0px; }
.stButton>button { background-color: #E50914; color: white; border-radius: 8px; width: 100%; font-weight: bold; border: none; }
.stButton>button:hover { background-color: #f6121d; color: white; }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# --- 2. API POSTER FETCH FUNCTION ---
def fetch_poster(movie_id):
    # PASTE YOUR API KEY BETWEEN THESE QUOTES:
    api_key = "8c4de29272af83ae235d4f173b323d16" 
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    try:
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception:
        pass
    
    # Fallback image if TMDB is down or missing a poster
    return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"


# --- 3. RECOMMENDATION ENGINE ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movie_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_movie_posters


# --- 4. DATA LOADING ---
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


# --- 5. USER INTERFACE LAYOUT ---
st.title('🎬 Movie Recommender')
st.markdown("<p style='text-align: center; color: #a9a9a9;'>Discover films tailored to your cinematic taste.</p>", unsafe_allow_html=True)
st.write("") 

left_spacer, main_col, right_spacer = st.columns([1, 2, 1])
with main_col:
    selected_movie_name = st.selectbox('Select a movie you love:', movies['title'].values)
    st.write("") 
    submit_button = st.button('Generate Matches')


# --- 6. DISPLAY RESULTS ---
if submit_button:
    names, posters = recommend(selected_movie_name)
    
    st.write("---")
    st.markdown("<h3 style='text-align: center; color: white; margin-bottom: 25px;'>Top 5 Matches For You:</h3>", unsafe_allow_html=True)
    
    # Generate 5 side-by-side columns
    cols = st.columns(5)
    
    for idx, col in enumerate(cols):
        with col:
            # Render the image first, then the title directly beneath it
            st.image(posters[idx])
            st.markdown(f"<p style='text-align: center; font-weight: bold; color: white;'>{names[idx]}</p>", unsafe_allow_html=True)