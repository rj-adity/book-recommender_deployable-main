# 🚀 **Hugging Face Spaces Deployment Guide**

This guide will help you deploy your Book Recommender System to Hugging Face Spaces, which is often easier and more reliable than other platforms.

## ✨ **Why Hugging Face Spaces?**

- **🎯 Purpose-built** for machine learning applications
- **🆓 Free hosting** with generous limits
- **🔧 Easy deployment** with one-click setup
- **📱 Built-in API access** with public URLs
- **📊 Automatic monitoring** and scaling
- **🌐 Global CDN** for fast access worldwide

## 📋 **Prerequisites**

1. **Hugging Face Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **GitHub Repository**: Your project should be in a Git repository
3. **Generated Models**: Make sure you have all the `.pkl` files

## 🗂️ **Required Files Structure**

Your project should have this structure:
```
book-recommender/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── README.md                # Project description
├── Books.csv                # Book dataset
├── Users.csv                # User dataset
├── Ratings.csv              # Ratings dataset
├── popular.pkl              # Popularity model
├── pt.pkl                   # Pivot table model
├── books.pkl                # Books data model
└── similarity_scores.pkl    # Similarity matrix
```

## 🚀 **Step-by-Step Deployment**

### **Step 1: Create a New Space**

1. **Go to [huggingface.co/spaces](https://huggingface.co/spaces)**
2. **Click "Create new Space"**
3. **Fill in the details**:
   - **Owner**: Your username
   - **Space name**: `book-recommender-system` (or any name you prefer)
   - **License**: Choose appropriate license
   - **Space SDK**: Select **"Gradio"** (recommended for APIs)
   - **Space hardware**: Choose **"CPU"** (free tier)

### **Step 2: Configure Your Space**

1. **After creating the Space**, you'll see a setup page
2. **Choose "Upload files"** option
3. **Upload all your project files**:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - All CSV files
   - All `.pkl` files

### **Step 3: Create Space Configuration**

Create a file called `app.py` in your Space (this will be different from your Flask app):

```python
import gradio as gr
import requests
import json

# Your Space will run the Flask app, but Gradio provides a nice interface
def get_popular_books():
    try:
        response = requests.get("http://localhost:7860/popular")
        data = response.json()
        return json.dumps(data, indent=2)
    except:
        return "Error: API not available"

def get_recommendations(book_name):
    try:
        response = requests.get(f"http://localhost:7860/recommend/{book_name}")
        data = response.json()
        return json.dumps(data, indent=2)
    except:
        return "Error: API not available"

def search_books(query):
    try:
        response = requests.get(f"http://localhost:7860/search/{query}")
        data = response.json()
        return json.dumps(data, indent=2)
    except:
        return "Error: API not available"

# Create Gradio interface
with gr.Blocks(title="Book Recommender System") as demo:
    gr.Markdown("# 📚 Book Recommender System")
    gr.Markdown("Get book recommendations and search for your favorite books!")
    
    with gr.Tab("Popular Books"):
        gr.Markdown("## 🏆 Top 50 Popular Books")
        popular_btn = gr.Button("Get Popular Books")
        popular_output = gr.Textbox(label="Popular Books", lines=10)
        popular_btn.click(get_popular_books, outputs=popular_output)
    
    with gr.Tab("Get Recommendations"):
        gr.Markdown("## 🔍 Get Book Recommendations")
        book_input = gr.Textbox(label="Enter Book Title", placeholder="e.g., 1984")
        recommend_btn = gr.Button("Get Recommendations")
        recommend_output = gr.Textbox(label="Recommendations", lines=10)
        recommend_btn.click(get_recommendations, inputs=book_input, outputs=recommend_output)
    
    with gr.Tab("Search Books"):
        gr.Markdown("## 🔎 Search for Books")
        search_input = gr.Textbox(label="Search Query", placeholder="e.g., harry potter")
        search_btn = gr.Button("Search")
        search_output = gr.Textbox(label="Search Results", lines=10)
        search_btn.click(search_books, inputs=search_input, outputs=search_output)

demo.launch()
```

### **Step 4: Update Requirements**

Make sure your `requirements.txt` includes:
```
Flask>=2.3.0
flask-cors>=4.0.0
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
gunicorn>=21.0.0
Werkzeug>=2.3.0
gradio>=4.0.0
requests>=2.28.0
```

### **Step 5: Deploy**

1. **Commit your changes** to the Space
2. **Wait for build** to complete (usually 2-5 minutes)
3. **Your Space will be live** at: `https://huggingface.co/spaces/YOUR_USERNAME/book-recommender-system`

## 🌐 **Accessing Your API**

### **Direct API Access**
Your Flask API will be available at:
- **Base URL**: `https://YOUR_USERNAME-book-recommender-system.hf.space`
- **Health Check**: `/health`
- **Popular Books**: `/popular`
- **Recommendations**: `/recommend/<book_name>`
- **Search**: `/search/<query>`

### **Gradio Interface**
The user-friendly interface will be at:
`https://huggingface.co/spaces/YOUR_USERNAME/book-recommender-system`

## 🔧 **Troubleshooting**

### **Common Issues**

1. **Build Fails**:
   - Check `requirements.txt` for compatibility
   - Ensure all files are uploaded
   - Check build logs for specific errors

2. **Models Not Loading**:
   - Verify all `.pkl` files are uploaded
   - Check file sizes (should be several MB)
   - Ensure CSV files are present

3. **API Not Responding**:
   - Wait for build to complete
   - Check Space status in dashboard
   - Verify port configuration

### **Monitoring**

- **Check Space status** in your Hugging Face dashboard
- **View build logs** for any errors
- **Monitor API performance** through the interface

## 🎯 **Testing Your Deployment**

1. **Visit your Space URL**
2. **Test the Gradio interface**:
   - Click "Get Popular Books"
   - Try getting recommendations for "1984"
   - Search for "harry potter"
3. **Test direct API calls**:
   - Use tools like Postman or curl
   - Test all endpoints

## 🚀 **Next Steps After Deployment**

1. **Share your Space URL** with others
2. **Integrate with other applications** using the API
3. **Monitor usage** in Hugging Face dashboard
4. **Update models** by re-uploading files

## 💡 **Pro Tips**

- **Use descriptive Space names** for better discoverability
- **Add tags** to your Space for categorization
- **Include examples** in your README
- **Monitor resource usage** to stay within free tier limits

---

**🎉 Congratulations!** Your Book Recommender System will now be accessible worldwide through Hugging Face Spaces!

**Need help?** Check the Hugging Face documentation or community forums for additional support. 