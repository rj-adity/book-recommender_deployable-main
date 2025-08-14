#!python
"""
Script to generate the pickle files needed for the book recommender system.
This script replicates the exact logic from Book_recommender.ipynb
"""

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import os

def generate_models():
    """Generate all the pickle files needed for the recommender system"""
    
    print("Book Recommender System - Model Generator")
    print("=" * 50)
    print("Loading data...")
    
    # Check if CSV files exist
    required_files = ['Books.csv', 'Users.csv', 'Ratings.csv']
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"Warning: Missing CSV files: {missing_files}")
        print("Please ensure all CSV files are present in the current directory.")
        return False
    
    try:
        # Load the CSV files with correct separator (semicolon) and encoding
        try:
            books = pd.read_csv('Books.csv', encoding='latin-1', sep=';', on_bad_lines='skip')
        except:
            books = pd.read_csv('Books.csv', sep=';', on_bad_lines='skip')
        
        try:
            users = pd.read_csv('Users.csv', encoding='latin-1', sep=';', on_bad_lines='skip')
        except:
            users = pd.read_csv('Users.csv', sep=';', on_bad_lines='skip')
            
        try:
            ratings = pd.read_csv('Ratings.csv', encoding='latin-1', sep=';', on_bad_lines='skip')
        except:
            ratings = pd.read_csv('Ratings.csv', sep=';', on_bad_lines='skip')
        
        print(f"Loaded {len(books)} books, {len(users)} users, {len(ratings)} ratings")
        
        # Check column names to debug
        print(f"Books columns: {list(books.columns)}")
        print(f"Ratings columns: {list(ratings.columns)}")
        print(f"Users columns: {list(users.columns)}")
        
        # Generate Popularity Based Recommender (exactly as in notebook)
        print("Generating popularity-based recommendations...")
        ratings_with_name = ratings.merge(books, on='ISBN')
        
        # Get number of ratings per book
        num_rating_df = ratings_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
        num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)
        
        # Convert ratings to numeric and handle non-numeric values (as in notebook)
        ratings_with_name['Book-Rating'] = pd.to_numeric(ratings_with_name['Book-Rating'], errors='coerce')
        ratings_with_name.dropna(subset=['Book-Rating'], inplace=True)
        
        # Get average rating per book
        avg_rating_df = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
        avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)
        
        # Merge and filter popular books (min 250 ratings) - exactly as in notebook
        popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')
        popular_df = popular_df[popular_df['num_ratings'] >= 250].sort_values('avg_rating', ascending=False).head(50)
        popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']]
        
        print(f"Generated popularity recommendations for {len(popular_df)} books")
        
        # Generate Collaborative Filtering Based Recommender (exactly as in notebook)
        print("Generating collaborative filtering recommendations...")
        
        # Filter users with more than 200 ratings
        x = ratings_with_name.groupby('User-ID').count()['Book-Rating'] > 200
        padhe_likhe_users = x[x].index
        
        # Filter ratings for these users
        filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(padhe_likhe_users)]
        
        # Filter books with more than 50 ratings
        y = filtered_rating.groupby('Book-Title').count()['Book-Rating'] >= 50
        famous_books = y[y].index
        
        # Get final ratings
        final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]
        
        # Create pivot table
        pt = final_ratings.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')
        pt.fillna(0, inplace=True)
        
        # Calculate similarity scores
        similarity_scores = cosine_similarity(pt)
        
        print(f"Generated collaborative filtering for {len(pt)} books with {similarity_scores.shape[0]} similarity scores")
        
        # Save all models to pickle files (exactly as in notebook)
        print("Saving models to pickle files...")
        
        pickle.dump(popular_df, open('popular.pkl', 'wb'))
        pickle.dump(pt, open('pt.pkl', 'wb'))
        pickle.dump(books, open('books.pkl', 'wb'))
        pickle.dump(similarity_scores, open('similarity_scores.pkl', 'wb'))
        
        print("All models saved successfully!")
        print("Files created:")
        print("- popular.pkl")
        print("- pt.pkl") 
        print("- books.pkl")
        print("- similarity_scores.pkl")
        
        return True
        
    except Exception as e:
        print(f"Error generating models: {str(e)}")
        import traceback
        print("Full error details:")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = generate_models()
    
    if success:
        print("\n✅ Models generated successfully! You can now deploy to Railway.")
    else:
        print("\n❌ Failed to generate models. Please check the error messages above.") 