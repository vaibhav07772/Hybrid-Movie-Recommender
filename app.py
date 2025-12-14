import streamlit as st
from recommender import hybrid_recommendation, movies, user_movie_matrix

st.title("🎬 Hybrid Movie Recommendation System")

# Sidebar Inputs
user_id = st.sidebar.number_input("Enter User ID", 
                                  min_value=int(user_movie_matrix.index.min()), 
                                  max_value=int(user_movie_matrix.index.max()), value=1)
movie_name = st.sidebar.selectbox("Select a Movie", movies['title'].tolist())
alpha = st.sidebar.slider("Collaborative vs Content Weight (α)", 0.0, 1.0, 0.5, 0.1)

# Recommendation Button
if st.sidebar.button("Recommend Movies"):
    recommendations = hybrid_recommendation(user_id, movie_name, n=5, alpha=alpha)
    st.subheader(f"Top Recommendations for User {user_id} based on '{movie_name}'")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. {movie}")