# 📚 Book Recommender System - Project Structure

## 🗂️ **Project Overview**
A machine learning-based book recommendation system that provides both popularity-based and collaborative filtering recommendations. Designed for deployment on Hugging Face Spaces.

## 📁 **File Structure**

```
book-recommender/
├── 📄 app.py                    # Flask API backend
├── 📄 gradio_app.py            # Gradio user interface
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                # Project documentation
├── 📄 HUGGINGFACE_DEPLOYMENT.md # Deployment guide
├── 📄 deploy_to_huggingface.py # Deployment helper script
├── 📄 PROJECT_STRUCTURE.md     # This file
├── 📊 Books.csv                # Book dataset (74MB)
├── 📊 Users.csv                # User dataset (12MB)
├── 📊 Ratings.csv              # Ratings dataset (29MB)
├── 🧠 popular.pkl              # Popularity model (7.6KB)
├── 🧠 pt.pkl                   # Pivot table model (4.4MB)
├── 🧠 books.pkl                # Books data model (68MB)
└── 🧠 similarity_scores.pkl    # Similarity matrix (3.8MB)
```

## 🎯 **Core Components**

### **Backend API (`app.py`)**
- Flask-based REST API
- Provides book recommendations
- Handles search functionality
- Health monitoring endpoints

### **User Interface (`gradio_app.py`)**
- Beautiful Gradio interface
- Easy-to-use tabs for different features
- Real-time API testing
- User-friendly design

### **Machine Learning Models**
- **Popularity Model**: Top 50 books based on ratings
- **Collaborative Filtering**: Personalized recommendations
- **Search Engine**: Find books by title or author

## 🚀 **Deployment Ready**

This project is specifically configured for **Hugging Face Spaces**:
- ✅ All dependencies included
- ✅ Models pre-trained and ready
- ✅ Interface optimized for web deployment
- ✅ No external hosting requirements

## 🔧 **Technologies Used**

- **Python 3.9+**
- **Flask** - Web API framework
- **Gradio** - User interface
- **Pandas & NumPy** - Data processing
- **Scikit-learn** - Machine learning algorithms
- **Pickle** - Model serialization

## 📱 **Features**

1. **🏆 Popular Books**: Get top 50 most popular books
2. **🔍 Recommendations**: Find similar books to your favorites
3. **🔎 Search**: Search books by title or author
4. **💚 Health Check**: Monitor system status
5. **📊 API Access**: Full REST API for integration

## 🌐 **Deployment Benefits**

- **Free hosting** on Hugging Face Spaces
- **Global CDN** for fast access worldwide
- **Automatic scaling** and monitoring
- **Beautiful interface** for end users
- **API access** for developers

## 📖 **Getting Started**

1. **Run locally**: `python app.py` (for development)
2. **Deploy to HF**: Use the deployment script
3. **Test interface**: Visit your Space URL
4. **Use API**: Integrate with other applications

---

**Note**: This project is optimized for Hugging Face Spaces deployment and provides a complete, production-ready book recommendation system. 