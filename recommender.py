import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")
df = pd.merge(ratings, movies, on="movieId")

# User-Movie Matrix
user_movie_matrix = df.pivot_table(index='userId', columns='title', values='rating').fillna(0)

# Item-based similarity
item_similarity = cosine_similarity(user_movie_matrix.T)
item_similarity_df = pd.DataFrame(item_similarity, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Content-based similarity
tfidf = TfidfVectorizer(stop_words='english')
movies['genres'] = movies['genres'].replace("(no genres listed)", "")
tfidf_matrix = tfidf.fit_transform(movies['genres'])
content_similarity = cosine_similarity(tfidf_matrix)
content_similarity_df = pd.DataFrame(content_similarity, index=movies['title'], columns=movies['title'])

# Hybrid Recommendation Function
def hybrid_recommendation(user_id, movie_name, n=5, alpha=0.5):
    if movie_name not in item_similarity_df.columns:
        return "Movie not found"
    
    collab_scores = item_similarity_df[movie_name]
    content_scores = content_similarity_df[movie_name]
    hybrid_scores = (alpha * collab_scores) + ((1 - alpha) * content_scores)
    
    watched = user_movie_matrix.loc[user_id]
    watched = watched[watched > 0].index
    
    recommendations = hybrid_scores.drop(watched).sort_values(ascending=False)
    return recommendations.head(n).index.tolist()