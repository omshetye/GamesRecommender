import streamlit as st
import pickle
import pandas

games_list=pickle.load(open('games.pkl', 'rb'))
games_list=games_list['Title'].values
st.title('Video Games Recommender System')
choice = st.selectbox("Pick one", games_list)