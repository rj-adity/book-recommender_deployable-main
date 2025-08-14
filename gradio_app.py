import gradio as gr
import requests
import json

# Your Space will run the Flask app, but Gradio provides a nice interface
def get_popular_books():
    """Get popular books from the Flask API"""
    try:
        response = requests.get("http://localhost:7860/popular")
        data = response.json()
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: API not available - {str(e)}"

def get_recommendations(book_name):
    """Get book recommendations from the Flask API"""
    if not book_name.strip():
        return "Please enter a book title"
    
    try:
        response = requests.get(f"http://localhost:7860/recommend/{book_name}")
        data = response.json()
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: API not available - {str(e)}"

def search_books(query):
    """Search for books using the Flask API"""
    if not query.strip():
        return "Please enter a search query"
    
    try:
        response = requests.get(f"http://localhost:7860/search/{query}")
        data = response.json()
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: API not available - {str(e)}"

def check_health():
    """Check API health status"""
    try:
        response = requests.get("http://localhost:7860/health")
        data = response.json()
        return json.dumps(data, indent=2)
    except Exception as e:
        return f"Error: API not available - {str(e)}"

# Create Gradio interface
with gr.Blocks(title="📚 Book Recommender System", theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 📚 Book Recommender System
    
    Welcome to the Book Recommender System! This system provides both popularity-based and collaborative filtering recommendations.
    
    ## 🎯 Features
    - **Popular Books**: Get top 50 most popular books
    - **Personalized Recommendations**: Find books similar to your favorites
    - **Book Search**: Search for books by title or author
    - **Health Check**: Monitor system status
    """)
    
    with gr.Tab("🏆 Popular Books"):
        gr.Markdown("## Get the most popular books based on user ratings")
        popular_btn = gr.Button("📊 Get Popular Books", variant="primary")
        popular_output = gr.Textbox(
            label="Popular Books", 
            lines=15, 
            placeholder="Click the button to get popular books..."
        )
        popular_btn.click(get_popular_books, outputs=popular_output)
    
    with gr.Tab("🔍 Get Recommendations"):
        gr.Markdown("## Get personalized book recommendations")
        gr.Markdown("Enter a book title to find similar books you might enjoy")
        book_input = gr.Textbox(
            label="Book Title", 
            placeholder="e.g., 1984, Harry Potter, The Great Gatsby"
        )
        recommend_btn = gr.Button("🎯 Get Recommendations", variant="primary")
        recommend_output = gr.Textbox(
            label="Recommendations", 
            lines=15,
            placeholder="Enter a book title and click the button..."
        )
        recommend_btn.click(get_recommendations, inputs=book_input, outputs=recommend_output)
    
    with gr.Tab("🔎 Search Books"):
        gr.Markdown("## Search for books by title or author")
        gr.Markdown("Find books that match your search criteria")
        search_input = gr.Textbox(
            label="Search Query", 
            placeholder="e.g., harry potter, jk rowling, fantasy"
        )
        search_btn = gr.Button("🔍 Search", variant="primary")
        search_output = gr.Textbox(
            label="Search Results", 
            lines=15,
            placeholder="Enter a search query and click the button..."
        )
        search_btn.click(search_books, inputs=search_input, outputs=search_output)
    
    with gr.Tab("💚 Health Check"):
        gr.Markdown("## Monitor system health and model status")
        gr.Markdown("Check if all models are loaded and the system is running properly")
        health_btn = gr.Button("🏥 Check Health", variant="primary")
        health_output = gr.Textbox(
            label="System Health", 
            lines=10,
            placeholder="Click the button to check system health..."
        )
        health_btn.click(check_health, outputs=health_output)
    
    with gr.Tab("ℹ️ About"):
        gr.Markdown("""
        ## About This System
        
        This Book Recommender System uses two recommendation strategies:
        
        ### 🏆 Popularity-Based Recommendations
        - Shows TOP 50 books with highest average ratings
        - Minimum of 250 votes required
        - Based on overall user popularity and ratings
        
        ### 🤝 Collaborative Filtering
        - Considers users with minimum of 200 ratings
        - Books must have been rated by more than 50 users
        - Uses cosine similarity for personalized recommendations
        
        ### 🛠️ Technical Details
        - **Backend**: Flask API with machine learning models
        - **Frontend**: Gradio interface for easy interaction
        - **Models**: Pre-trained using pandas, numpy, and scikit-learn
        - **Data**: Based on real book ratings and user data
        
        ### 📱 How to Use
        1. **Popular Books**: Click to see trending books
        2. **Recommendations**: Enter a book title to get similar suggestions
        3. **Search**: Find books by title or author
        4. **Health**: Monitor system status
        
        ### 🔗 API Endpoints
        - `/popular` - Get popular books
        - `/recommend/<book_name>` - Get recommendations
        - `/search/<query>` - Search books
        - `/health` - System health check
        """)

# Launch the interface
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
else:
    demo.launch() 