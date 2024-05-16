import pickle
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors

st.header("Recipe Recommendation System")
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
dataset = pickle.load(open('dataset.pkl', 'rb'))
image = pickle.load(open('image.pkl', 'rb'))
ingredient = pickle.load(open('ingredient.pkl', 'rb'))
info = pickle.load(open('info.pkl', 'rb'))
recipeName = pickle.load(open('recipeName.pkl', 'rb'))

# Function to generate recommendations based on knn
def generate_knn_recommendations(item_id, df, knn_model, n_neighbors=10):
    #item_index = df[df['item_id'] == item_id].index[0]
    item_index = item_id
    distances, indices = knn_model.kneighbors(tfidf[item_index], n_neighbors=n_neighbors + 1)
    similar_items = df.iloc[indices[0][1:]]  # Menghapus item itu sendiri dari hasil
    return similar_items



# Contoh penggunaan: merekomendasikan item berdasarkan item_id 1
recommendations = generate_knn_recommendations(96, info, model)
print("Recommendations based on item_id 1:")

df = recommendations
# Display the DataFrame without index
#df = df.style.hide_index()
st.dataframe(df, hide_index = True)
