from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for Hugging Face Spaces

# Load the pre-trained models and data
try:
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    pt = pickle.load(open('pt.pkl', 'rb'))
    books = pickle.load(open('books.pkl', 'rb'))
    similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
    print("✅ All models loaded successfully!")
except FileNotFoundError as e:
    print(f"❌ Model file not found: {e}")
    popular_df = None
    pt = None
    books = None
    similarity_scores = None

@app.route('/')
def home():
    return jsonify({
        "message": "Book Recommender System API",
        "status": "running",
        "models_loaded": {
            "popular_df": popular_df is not None,
            "pt": pt is not None,
            "books": books is not None,
            "similarity_scores": similarity_scores is not None
        },
        "endpoints": {
            "popular_books": "/popular",
            "recommend_books": "/recommend/<book_name>",
            "search_books": "/search/<query>",
            "health": "/health"
        }
    })

@app.route('/popular')
def get_popular_books():
    """Get top 50 popular books"""
    if popular_df is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Convert to list of dictionaries for JSON serialization
        popular_books = []
        for _, row in popular_df.iterrows():
            popular_books.append({
                "title": row['Book-Title'],
                "author": row['Book-Author'],
                "image_url": row['Image-URL-M'],
                "num_ratings": int(row['num_ratings']),
                "avg_rating": float(row['avg_rating'])
            })
        
        return jsonify({
            "message": "Top 50 Popular Books",
            "count": len(popular_books),
            "books": popular_books
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommend/<book_name>')
def recommend_books(book_name):
    """Get book recommendations based on a book name"""
    if pt is None or books is None or similarity_scores is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Check if book exists in our dataset
        if book_name not in pt.index:
            return jsonify({"error": f"Book '{book_name}' not found in dataset"}), 404
        
        # Get recommendations
        index = np.where(pt.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_scores[index])), 
                             key=lambda x: x[1], reverse=True)[1:6]  # Get top 5 recommendations
        
        recommendations = []
        for i in similar_items:
            book_title = pt.index[i[0]]
            temp_df = books[books['Book-Title'] == book_title]
            
            if not temp_df.empty:
                book_data = temp_df.drop_duplicates('Book-Title').iloc[0]
                recommendations.append({
                    "title": book_data['Book-Title'],
                    "author": book_data['Book-Author'],
                    "image_url": book_data['Image-URL-M'],
                    "similarity_score": float(i[1])
                })
        
        return jsonify({
            "message": f"Recommendations for '{book_name}'",
            "input_book": book_name,
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search/<query>')
def search_books(query):
    """Search for books by title or author"""
    if books is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    try:
        # Search in book titles and authors
        query_lower = query.lower()
        matching_books = books[
            (books['Book-Title'].str.lower().str.contains(query_lower, na=False)) |
            (books['Book-Author'].str.lower().str.contains(query_lower, na=False))
        ].drop_duplicates('Book-Title').head(20)
        
        search_results = []
        for _, row in matching_books.iterrows():
            search_results.append({
                "title": row['Book-Title'],
                "author": row['Book-Author'],
                "image_url": row['Image-URL-M'],
                "publisher": row['Publisher'],
                "year": row['Year-Of-Publication']
            })
        
        return jsonify({
            "message": f"Search results for '{query}'",
            "query": query,
            "count": len(search_results),
            "books": search_results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        "status": "healthy",
        "models_loaded": {
            "popular_df": popular_df is not None,
            "pt": pt is not None,
            "books": books is not None,
            "similarity_scores": similarity_scores is not None
        }
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7860))  # Hugging Face uses port 7860
    app.run(host='0.0.0.0', port=port, debug=False) 