import pandas as pd
import streamlit as st
import pickle
import requests
from io import BytesIO
from PIL import Image
def recommend(game):
    game_index=games[games['Title']==game].index[0]
    dist=sim_mat[game_index]
    games_list=sorted(list(enumerate(dist)), reverse=True, key=lambda x:x[1])[1:7]
    recommended=[]
    recommended_posters=[]
    for i in games_list:
        recommended.append(games.iloc[i[0]].Title)
        recommended_posters.append(get_poster(games.iloc[i[0]].Title, api_key))
    return recommended, recommended_posters


def get_poster(game, api_key):
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


api_key = "93a4c88f89e54c249635f2e12a2cbd8f"
games_dict=pickle.load(open('games.pkl', 'rb'))
games=pd.DataFrame(games_dict)
sim_mat=pickle.load(open('sim.pkl', 'rb'))
st.title("Om's Video Gamer Recommender System")
game_selected = st.selectbox("Pick one", games['Title'].values)
st.sidebar.title("Sidebar Title")
st.sidebar.text("Sidebar content")
if st.button("Recommend"):
    names, posters=recommend(game_selected)
    col1, col2 = st.columns(2)
    with col1:
        for i in range(0, 6, 2):
            st.text(names[i])
            response=requests.get(posters[i])
            img=Image.open(BytesIO(response.content))
            img=img.resize((400, 200))
            st.image(img)
            st.markdown("<hr>", unsafe_allow_html=True)
    with col2:
        for i in range(1, 6, 2):
            st.text(names[i])
            response = requests.get(posters[i])
            img = Image.open(BytesIO(response.content))
            img = img.resize((400, 200))
            st.image(img)
            st.markdown("<hr>", unsafe_allow_html=True)