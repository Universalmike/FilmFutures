import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px
import pickle
import requests
from Ddetails import movie_details, movie_info, blog_title, blog_details

types = ['MOVIE', 'SHOW']

#load the model
with open("movie-imdb-score-predictor2", "rb") as f:
    model = pickle.load(f)

def predict_imdb_score(input_data):
    # Create a DataFrame for the input features
    input_df = pd.DataFrame(input_data)
    return model.predict(input_df)

#load the .env file
load_dotenv()

#Retrieve api key
api_key = os.getenv("api_key")

# Function to get movie details from TMDb
def get_movie_details(movie_title):
    base_url = 'https://api.themoviedb.org/3'
    search_url = f'{base_url}/search/movie'

    # Parameters for the request
    params = {
        'api_key': api_key,
        'query': movie_title
    }

    # Make the request
    response = requests.get(search_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        movie_data = response.json()

        # Fetch detailed information about the first movie result
        if movie_data['results']:
            first_movie = movie_data['results'][0]
            movie_id = first_movie['id']
            details_url = f'{base_url}/movie/{movie_id}'
            details_params = {
                'api_key': api_key
            }
            details_response = requests.get(details_url, params=details_params)
            return details_response.json()
        else:
            st.error("Movie not found.")
            return {}
    else:
        st.error(f"Error: {response.status_code}")
        return {}

# Page configuration
st.set_page_config(page_title='FilmFutures', layout='wide')

# Custom CSS for styling
st.markdown(
    """
    <style>
    .top-bar {
        background-color: red;
        padding: 10px;
        display: flex;
        flex-wrap: wrap;  /* Allow wrapping on smaller screens */
        justify-content: space-between;
        align-items: center;
    }
    .top-bar a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
        font-size: 1em;  /* Relative size for better scaling */
    }
    .top-bar h1 {
        margin: 0;
        padding: 0;
        color: white;
        font-size: 1.5em;  /* Use relative sizes */
    }
    .section-header {
        background-color: red;
        padding: 10px;
        border-radius: 5px;
        color: white;
        text-align: center;
    }
    .movie-input, .upcoming-movies, .top-rated-movies, .blog, .contact-us {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Top navigation bar
st.markdown(
    """
    <div class="top-bar">
        <h1>FilmFutures</h1>
        <div>
            <a href="#movie-input">Check Movie Ratings</a>
            <a href="#upcoming-movies">Upcoming Movies</a>
            <a href="#top-rated-movies">Top Rated Movies</a>
            <a href="#blog">Blog</a>
            <a href="#contact-us">Contact Us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Predict function
def predict_imdb_score(input_data):
    # Create a DataFrame for the input features
    input_df = pd.DataFrame(input_data)
    return model.predict(input_df)

# Movie input form
st.markdown("<h1 id='movie-input'>Curious about movies rating? Predict it now!</h1>", unsafe_allow_html=True)
movie_title = st.text_input('Movie Title:')

# Fetch movie details if a title is entered
if movie_title:
    movie_data = get_movie_details(movie_title)
    
    if movie_details:
        # Auto-fill other fields with corresponding details
        release_date = movie_data.get('release_date', 'N/A')
        genres = ', '.join([genre['name'] for genre in movie_data.get('genres', [])]) if movie_data.get('genres') else 'Unknown'
        runtime = movie_data.get('runtime', 'Unknown')
        production_countries = ', '.join([country['name'] for country in movie_data.get('production_countries', [])]) if movie_data.get('production_countries') else 'Unknown'
        age_certification = movie_data.get('certification', 'N/A') if 'certification' in movie_data else 'Unknown'
        
        
        st.text_input('Release Date:', value=release_date)
        st.text_input('Genre:', value=genres)
        st.text_input('Runtime:', value=runtime)
        st.text_input('Age Certification:', value=age_certification)
        st.text_input('Production Country:', value=production_countries)

type_ = st.selectbox('Type:', types)

    
submit_button = st.button('Predict')

if submit_button:
    if not all([movie_title, release_date, type_, age_certification, runtime, genres, production_countries]):
        st.warning('Please enter all features for the movie.')
    else:
        input_data = [{
            'type': type_,
            'age_certification': age_certification,
            'runtime': runtime,
            'genres': genres,
            'production_countries': production_countries
        }]
        prediction = predict_imdb_score(input_data)[0]
        st.markdown(f"""
        <div class="movie-input">
            <p>Title: {movie_title}</p>
            <p>Release Date: {release_date}</p>
            <p>Predicted IMDb score: {prediction:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

# Upcoming movies
st.markdown("<h2 id='upcoming-movies'>Upcoming Movies</h2>", unsafe_allow_html=True)
upcoming_movies = [
    {'title': movie_details(1), 'content': movie_info(1)},
    {'title': movie_details(2), 'content':  movie_info(2)},
    {'title': movie_details(3), 'content': movie_info(3)},
    {'title': movie_details(4), 'content': movie_info(4)},
    {'title': movie_details(5), 'content': movie_info(5)}
]
for movie in upcoming_movies:
    if st.button(movie['title']):
        st.markdown(f"<div class='upcoming-movies'>{movie['content']}</div>", unsafe_allow_html=True)

# Top rated movies
st.markdown("<h2 id='top-rated-movies'>Top Rated Movies in Each Country</h2>", unsafe_allow_html=True)
country_movie_data = [
    {'country': 'USA', 'movies': [{'title': 'Dune: Part Two', 'rating': 8.6}, {'title': 'Furiosa: A Mad Max Saga', 'rating': 7.7}, {'title': 'Deadpool & Wolverine', 'rating': 8.0}, {'title': 'The Substance', 'rating': 8.0}, {'title': 'Transformers One', 'rating': 7.9}]},
    {'country': 'UK', 'movies': [{'title': 'Monkey Man', 'rating': 6.9}, {'title': 'Kill', 'rating': 7.9}, {'title': 'Alien: Romulus', 'rating': 7.4}, {'title': 'Kneecap', 'rating': 7.6}, {'title': 'Supacell', 'rating': 7.0}]},
    {'country': 'Nigeria', 'movies': [{'title': 'The Silent Intruder', 'rating': 9.4}, {'title': 'Funmilayo Ransome-Kuti', 'rating': 8.7}, {'title': "All's Fair In Love", 'rating': 6.4}, {'title': 'Japa', 'rating': 7.3}]}
]
country_index = st.number_input('Select Country Index:', min_value=0, max_value=len(country_movie_data)-1, value=0)
country_data = country_movie_data[country_index]
fig = px.bar(
    pd.DataFrame(country_data['movies']),
    x='title',
    y='rating',
    title=f'Top Rated Movies in {country_data["country"]}',
    labels={'rating': 'IMDb Rating', 'title': 'Movie Title'},
    color='rating'
)
st.plotly_chart(fig)

# Blog section
st.markdown("<h2 id='blog'>Articles</h2>", unsafe_allow_html=True)
blogs = [
    {'title': blog_title(1), 'content': blog_details(1)},
    {'title': blog_title(2), 'content': blog_details(2)},
    {'title': blog_title(3), 'content': blog_details(3)}
]
for blog in blogs:
    if st.button(blog['title']):
        st.markdown(f"<div class='blog'>{blog['content']}</div>", unsafe_allow_html=True)

# Contact Us section
st.markdown("<h2 id='contact-us'>Contact Us</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact-us">
        <p>For any inquiries, please email us at: michaelologungbara@gmail.com or call +234 803 722 1447</p>
        <p>copyright: michael ologungbara</p>
    </div>
    """,
    unsafe_allow_html=True
)
