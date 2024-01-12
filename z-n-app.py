import pandas as pd
from flask import Flask, jsonify, request
from sklearn.metrics.pairwise import cosine_similarity
import pickle

app = Flask(__name__)

with open('vectors_tfidf.pkl', 'rb') as file:
    vectors_tfidf = pickle.load(file)

# Load Cosine Similarity Matrix
with open('similarity_tfidf.pkl', 'rb') as file:
    similarity = pickle.load(file)


def load_movie_names():
    # Load CSV file containing movie names
    df = pd.read_csv('C:/Users/User/RP2-CapstoneProject/data/preprocessed_data.csv')  # Replace 'movies.csv' with your file name
    return df['name'].tolist()  # Assuming 'name' is the column with movie names

movie_names = load_movie_names()  # Load movie names from the CSV

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    input_text = data.get('input_text', 'Chaplin')  # Assuming input comes as JSON with 'input_text' key

    # Transform input text into TF-IDF vector
    input_tfidf = vectors_tfidf.transform([input_text])

    # Calculate cosine similarity between input and movie data
    similarity_ = cosine_similarity(input_tfidf, vectors_tfidf)  # Assuming movies are in TF-IDF format

    # Get indices of most similar movies
    similar_movies_indices = similarity_.argsort()[:-4:-1]  # Get top 3 recommendations

    # Retrieve movie names based on indices or any relevant data
    recommendations = [movie_names[idx] for idx in similar_movies_indices]  # Replace with your data

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
