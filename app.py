import streamlit as st
import pandas as pd  
import pickle 


movies = pickle.load(open("movies_data.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

def get_recommendations(title): 
    if title not in movies['title'].values:
        return None 
    

    index = movies[movies['title']== title].index[0]
    distances = similarity[index]


    movies_list = sorted(list(enumerate(distances)),
                         reverse = True,
                         key = lambda x: x[1])[1:11]
    
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]])

    return pd.DataFrame(recommended_movies)    



st.title("MOVIE RECOMMENDATION SYSTEM")

selected_movie = st.selectbox("Select a movie:", movies["title"].values)

if st.button("Recommend"):
    recommendations = get_recommendations(selected_movie)
    

    
    for i in range(len(recommendations)):
            st.write(recommendations.iloc[i]["title"])

        
