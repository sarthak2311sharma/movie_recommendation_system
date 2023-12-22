import streamlit as st
import pickle
import pandas as pd
import requests
similarity=pickle.load(open('similarity.pkl','rb'))

movie_lists=pickle.load(open('movies_dict.pkl','rb'))
movie_list=pd.DataFrame(movie_lists)
print(movie_list)
st.title("MOVIE RECOMMENDER SYSTEM")

def fetch(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0970fddfd0ca7147521b6741e98e0fad&language=en-US'.format(movie_id))
    data=response.json()
    return 'http://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movies):
    index=movie_list[movie_list['title'] == movies].index[0]
    distance=similarity[index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended = []
    recommended_poster=[]
    for i in movies_list:
        movie_id=movie_list.iloc[i[0]].id
        recommended.append(movie_list.iloc[i[0]].title)
        recommended_poster.append(fetch(movie_id))
    return recommended,recommended_poster

option = st.selectbox('ENTER THE MOVIE NAME',movie_list['title'].values)
print(option)
if st.button("Recommend"):
    names,posters = recommend(option)
    col1, col2, col3 ,col4 ,col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])