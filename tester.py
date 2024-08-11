import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import requests

types = ['MOVIE', 'SHOW']
Cuckoo = (f"Stars: Hunter Schafer, Jan Bluthardt, Marton Csokas\n\n"
f"Reluctantly, 17-year-old Gretchen leaves her American home to live with her father, who has just moved into a resort in the German Alps with his new family. Arriving at their future residence, they are greeted by Mr. König, her father's boss, who takes an inexplicable interest in Gretchen's mute half-sister Alma. Something doesn't seem right in this tranquil vacation paradise. Gretchen is plagued by strange noises and bloody visions until she discovers a shocking secret that also concerns her own family.\n(credit: IMDB)")


The_Union = (f"Stars:  Mark Walhberg, Halle Berry.\n\n"
f"Mike (Wahlberg) is happy living a simple life as a construction worker in his native New Jersey –– until his long-lost high school sweetheart, Roxanne (Berry), shows up with more on her mind than romance. Knowing he’s the right man for the job, she recruits Mike on a dangerous intelligence mission in Europe that thrusts them back together into a world of spies and high-speed car chases, with sparks flying along the way (credit: Netflix)")

wolf = (f"Stars: Sarah Georgina, Elizabeth Nabben, Jennifer Saunders.\n\n"
f"Heroic poodle Freddy Lupin has everything it takes to lead his werewolf pack. Except respect. If only he were more... wolfish. But when a wayward wish transforms him into a werewolf and deposits a mischievous moon sprite on earth, Freddy must restore the cosmic order before earth and moon collide. Oops. One thing's for sure - Freddy will never question being a poodle again (cred: IMDB)")

ninenty_two = (f"Cast: Ray Liotta, Scott Eastwood, Tyrese Gibson\n\n"
f"In 1992, Mercer (Gibson) is desperately trying to rebuild his life and relationship with his son (Christopher A'mmanuel) amidst the turbulent 1992 L.A. uprising following the Rodney King verdict. Across town, another father and son (Liotta and Scott Eastwood) put their own strained relationship to the test as they plot a dangerous heist to steal catalytic converters, which contain valuable platinum, from the factory where Mercer works. As tensions rise in Los Angeles and chaos erupts, both families reach their boiling points when they collide. (credit: IMDD - Lionsgate)")

Incoming = (f"Cast: Raphael Alejandro, Bobby Cannavale, Kaitlin Olson\n\n"
f"Four freshmen navigate the terrors of adolescence at their first-ever high school party (credit: IMDB)")

Impact = "Movies have a profound impact on society, shaping cultural norms, influencing public opinion, and reflecting social issues.\n They serve as a powerful medium for storytelling, bringing diverse perspectives and fostering empathy.\nThrough their portrayal of characters, conflicts, and resolutions, films can inspire change, challenge stereotypes, and raise awareness about critical topics.\nAdditionally, movies offer a shared experience that unites audiences, sparking conversations and collective emotions.\nIn essence, cinema not only entertains but also educates and motivates, leaving a lasting imprint on societal values and individual lives."
print(Impact)

union = "Netflix's upcoming movie, The Union, promises to be an exhilarating addition to its action-thriller lineup. Starring Mark Wahlberg and Halle Berry, the film follows two ex-special forces operatives who reunite to tackle a high-stakes mission. With Wahlberg's charisma and Berry's fierce determination, their on-screen chemistry is set to captivate audiences. Directed by a renowned filmmaker known for crafting edge-of-your-seat narratives, The Union combines intense action sequences, gripping drama, and unexpected twists. Fans can anticipate a roller-coaster ride of emotions and adrenaline, making it a must-watch for thriller enthusiasts. Stay tuned for its release date and get ready for an unforgettable cinematic experience."

Dune = "Dune: Part 2 continues the epic saga of Arrakis, delivering a breathtaking sequel that surpasses its predecessor in every way. Directed by Denis Villeneuve, the film masterfully adapts Frank Herbert's complex narrative, delving deeper into the political intrigue and mystical elements of the Dune universe.Timothée Chalamet returns as Paul Atreides, now embracing his destiny as the prophesied leader. His performance is both commanding and nuanced, capturing the weight of his character's responsibilities. Zendaya’s role as Chani is expanded, offering a compelling portrayal of strength and resilience. The ensemble cast, including Rebecca Ferguson, Oscar Isaac, and Javier Bardem, adds depth and gravitas to the story.Visually, Dune: Part 2 is a spectacle. The sweeping desert landscapes and intricate set designs are brought to life with stunning cinematography. Hans Zimmer’s score complements the visuals perfectly, enhancing the film's epic scale and emotional impact.The film excels in balancing grandiose action sequences with intimate character moments. The climactic battles are intense and meticulously choreographed, while the quieter scenes explore themes of power, betrayal, and destiny.In conclusion, Dune: Part 2 is a cinematic triumph that solidifies the franchise’s place in sci-fi history. It’s a must-watch for fans and newcomers alike, promising a thrilling, thought-provoking experience."


with open("movie-imdb-score-predictor2", "rb") as f:
    model = pickle.load(f)

def predict_imdb_score(input_data):
    # Create a DataFrame for the input features
    input_df = pd.DataFrame(input_data)
    return model.predict(input_df)

# TMDB API KEY
api_key = '172555f2b8dc9d7b74e3ddbbe0b7160e'

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
        justify-content: space-between;
        align-items: center;
    }
    .top-bar a {
        color: white;
        text-decoration: none;
        margin: 0 10px;
    }
    .top-bar h1 {
        margin: 0;
        padding: 0;
        color: white;
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
    movie_details = get_movie_details(movie_title)
    
    if movie_details:
        # Auto-fill other fields with corresponding details
        release_date = movie_details.get('release_date', 'N/A')
        genres = ', '.join([genre['name'] for genre in movie_details.get('genres', [])]) if movie_details.get('genres') else 'Unknown'
        runtime = movie_details.get('runtime', 'Unknown')
        production_countries = ', '.join([country['name'] for country in movie_details.get('production_countries', [])]) if movie_details.get('production_countries') else 'Unknown'
        age_certification = movie_details.get('certification', 'N/A') if 'certification' in movie_details else 'Unknown'
        
        
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
    {'title': '1. CUCKOO (August 9th). Type: MOVIE. Age Rated: R. Runtime: 84m(1h24m). Genre(s): horror, mystery, thriller. Countries: Germany, United States', 'content': Cuckoo},
    {'title': '2. THE UNION (August 16). Type: MOVIE. Age Rated: R. Runtime: Unknown. Genre(s): thriller, action. Country: United States', 'content':  The_Union},
    {'title': '3. 200% wolf (August 8). Type: MOVIE. Age Rated: PG. Runtime: 98m(1h38m). Genre(s): animation, family. Countries: Australia, Germany, Spain, Mexico.', 'content': wolf},
    {'title': '4. 1992 (August 30th). Type: MOVIE. Age Rated: R. Runtime: Unknown. Genre(s): action, drama, thriller. Country: United Stats', 'content': ninenty_two},
    {'title': '5. Incoming (August 23). Type: MOVIE. Age Rated: R. Runtime: Unknown. Genre(s): comedy. Country: United States', 'content': Incoming}
]
for movie in upcoming_movies:
    if st.button(movie['title']):
        st.markdown(f"<div class='upcoming-movies'>{movie['content']}</div>", unsafe_allow_html=True)

# Top rated movies
st.markdown("<h2 id='top-rated-movies'>Top Rated Movies in Each Country</h2>", unsafe_allow_html=True)
country_movie_data = [
    {'country': 'USA', 'movies': [{'title': 'Dune: Part Two', 'rating': 8.6}, {'title': 'Furiosa: A Mad Max Saga', 'rating': 7.7}]},
    {'country': 'UK', 'movies': [{'title': 'Monkey Man', 'rating': 6.9}, {'title': 'Kill', 'rating': 7.9}]}
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
st.markdown("<h2 id='blog'>Blog</h2>", unsafe_allow_html=True)
blogs = [
    {'title': 'The Impact of Movies on Society', 'content': Impact},
    {'title': 'The Union: A Thrilling New Netflix Movie Starring Mark Wahlberg and Halle Berry', 'content': union},
    {'title': 'Dune: Part 2 - A Cinematic Triumph', 'content': Dune}
]
for blog in blogs:
    if st.button(blog['title']):
        st.markdown(f"<div class='blog'>{blog['content']}</div>", unsafe_allow_html=True)

# Contact Us section
st.markdown("<h2 id='contact-us'>Contact Us</h2>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="contact-us">
        <p>For any inquiries, please email us at: michaelologungbara@gmail.com</p>
        <p>copyright: supermic</p>
    </div>
    """,
    unsafe_allow_html=True
)
