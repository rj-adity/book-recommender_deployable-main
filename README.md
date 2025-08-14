# BOOK-RECOMMENDER-SYSTEM

A book recommender system that provides both popularity-based and collaborative filtering recommendations. This system can be deployed on Hugging Face Spaces for easy access.

## 🚀 **Deployment**

### **Hugging Face Spaces (Recommended)**
- **Easy deployment** with one-click setup
- **Free hosting** for machine learning applications
- **Built-in API access** with public URLs
- **Automatic scaling** and monitoring
- **Beautiful Gradio interface** for easy testing

## 📊 **RECOMMENDATION TYPES**

Recommendation systems can be categorized into 4 main types: 

1️⃣ **Popularity-based systems** - Highlight trending content like YouTube's trending section or IMDb's top movies

2️⃣ **Content-based systems** - Assess similarity based on attributes like actors or themes

3️⃣ **Collaborative filtering systems** - Rely on user ratings (what this system uses)

4️⃣ **Hybrid systems** - Like Netflix's, which combine multiple approaches to enhance recommendations

## 🔍 **FEATURES**

### **Popularity Based Recommendations**
- Shows TOP 50 books with Highest avg Rating
- Minimum of 250 votes required
- Based on overall user ratings and popularity

### **Collaborative Based Recommendations**
- Considers users with minimum of 200 ratings
- Books must have been voted by more than 50 users
- Uses cosine similarity for personalized recommendations

## 🌐 **API Endpoints**

Once deployed, your API will be available at:
- **Home**: `/` - API information and status
- **Health Check**: `/health` - System health and model status
- **Popular Books**: `/popular` - Top 50 popular books
- **Recommendations**: `/recommend/<book_name>` - Get book suggestions
- **Search**: `/search/<query>` - Search books by title or author

## 🛠️ **Skills & Technologies**
- Jupyter Notebook
- Python
- Machine Learning
- Recommendation system
- Flask API
- Hugging Face Spaces
- Pandas & NumPy
- Scikit-learn

## 🔗 **Links**
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sanika-nandurkar-7ab823250/)

## 📱 **Quick Start**

1. **Deploy to Hugging Face Spaces**:
   - Go to [huggingface.co/spaces](https://huggingface.co/spaces)
   - Create new Space
   - Choose "Gradio" template
   - Upload your files

2. **Test the API**:
   - Visit your Space URL
   - Use the beautiful Gradio interface
   - Test all endpoints
   - Enjoy your book recommendations!

---

**Note**: This system is designed to work without HTML/CSS files, providing a clean API-based solution that can be easily integrated into any application.
