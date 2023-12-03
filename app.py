import pandas as pd
import streamlit as st
import pickle
import requests
from io import BytesIO
from PIL import Image

# Load data and models
api_key = "93a4c88f89e54c249635f2e12a2cbd8f"
games_dict = pickle.load(open('games.pkl', 'rb'))
games = pd.DataFrame(games_dict)
sim_mat = pickle.load(open('sim.pkl', 'rb'))

st.sidebar.title("Welcome to GamerAI")
st.sidebar.text(
    "Explore a world of personalized gaming with our gaming recommendation system! "
    "Tailored to your preferences, it suggests diverse titles from the latest releases to hidden gems. "
    "Our user-friendly interface lets you seamlessly navigate recommendations, watch trailers, "
    "and access detailed game information. Stay ahead with real-time updates and connect with the gaming community "
    "through integrated feedback. Unlock achievements and milestones as you discover your next gaming obsession—all "
    "conveniently from our website's. Level up your gaming experience today!"
)

def recommend(game):
    game_index = games[games['Title'] == game].index[0]
    dist = sim_mat[game_index]
    games_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:7]
    recommended = []
    recommended_posters = []
    for i in games_list:
        recommended.append(games.iloc[i[0]].Title)
        recommended_posters.append(get_poster(games.iloc[i[0]].Title))
    return recommended, recommended_posters

def get_poster(game):
    base_url = "https://api.rawg.io/api/games"
    params = {"key": api_key, "search": game}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        games_list = data.get("results", [])

        if not games_list:
            st.warning("No games found. Try another title.")
            return None

        poster_url = games_list[0].get("background_image")
        return poster_url
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

st.title("Om's Video Gamer Recommender System")
game_selected = st.selectbox("Pick one", games['Title'].values)

if st.button("Recommend"):
    names, posters = recommend(game_selected)

    col1, col2 = st.columns(2)
    with col1:
        for i in range(0, 6, 2):
            st.text(names[i])
            if posters[i]:
                response = requests.get(posters[i])
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 200))
                st.image(img)
                st.markdown("<hr>", unsafe_allow_html=True)
    with col2:
        for i in range(1, 6, 2):
            st.text(names[i])
            if posters[i]:
                response = requests.get(posters[i])
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 200))
                st.image(img)
                st.markdown("<hr>", unsafe_allow_html=True)


# Load data and models
api_key = "93a4c88f89e54c249635f2e12a2cbd8f"
games_dict = pickle.load(open('games.pkl', 'rb'))
games = pd.DataFrame(games_dict)
sim_mat = pickle.load(open('sim.pkl', 'rb'))

st.sidebar.title("Welcome to GamerAI")
st.sidebar.text(
    "Explore a world of personalized gaming with our gaming recommendation system! "
    "Tailored to your preferences, it suggests diverse titles from the latest releases to hidden gems. "
    "Our user-friendly interface lets you seamlessly navigate recommendations, watch trailers, "
    "and access detailed game information. Stay ahead with real-time updates and connect with the gaming community "
    "through integrated feedback. Unlock achievements and milestones as you discover your next gaming obsession—all "
    "conveniently from our website's. Level up your gaming experience today!"
)

def recommend(game):
    game_index = games[games['Title'] == game].index[0]
    dist = sim_mat[game_index]
    games_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:7]
    recommended = []
    recommended_posters = []
    for i in games_list:
        recommended.append(games.iloc[i[0]].Title)
        recommended_posters.append(get_poster(games.iloc[i[0]].Title))
    return recommended, recommended_posters

def get_poster(game):
    base_url = "https://api.rawg.io/api/games"
    params = {"key": api_key, "search": game}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        games_list = data.get("results", [])

        if not games_list:
            st.warning("No games found. Try another title.")
            return None

        poster_url = games_list[0].get("background_image")
        return poster_url
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None

st.title("Om's Video Gamer Recommender System")
game_selected = st.selectbox("Pick one", games['Title'].values)

if st.button("Recommend"):
    names, posters = recommend(game_selected)

    col1, col2 = st.columns(2)
    with col1:
        for i in range(0, 6, 2):
            st.text(names[i])
            if posters[i]:
                response = requests.get(posters[i])
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 200))
                st.image(img)
                st.markdown("<hr>", unsafe_allow_html=True)
    with col2:
        for i in range(1, 6, 2):
            st.text(names[i])
            if posters[i]:
                response = requests.get(posters[i])
                img = Image.open(BytesIO(response.content))
                img = img.resize((400, 200))
                st.image(img)
                st.markdown("<hr>", unsafe_allow_html=True)
