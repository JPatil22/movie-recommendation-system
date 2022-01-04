import streamlit as st
import pickle
import requests


def fetch_posters(movie_id):
     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d4812daffcd5f272a463cff546893f10&language=en-US'
                             .format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

     recommended_movies = []
     recommended_posters = []

     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          recommended_movies.append(movies.iloc[i[0]].title)
# fetch poster from api
          recommended_posters.append(fetch_posters(movie_id))
     return recommended_movies, recommended_posters


movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('movie_recommend.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie = st.selectbox('How would you like to be contacted?', movies_list)

if st.button('RECOMMEND'):
     names, poster = recommend(selected_movie)

     col1, col2, col3, col4, col5 = st.columns(5)

     with col1:
          st.text(names[0])
          st.image(poster[0])
     with col2:
          st.text(names[1])
          st.image(poster[1])
     with col3:
          st.text(names[2])
          st.image(poster[2])
     with col4:
          st.text(names[3])
          st.image(poster[3])
     with col5:
          st.text(names[4])
          st.image(poster[4])
