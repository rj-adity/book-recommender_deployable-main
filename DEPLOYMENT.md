# Railway Deployment Guide for Book Recommender System

This guide will help you deploy the Book Recommender System to Railway without using HTML/CSS files.

## Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **Git Repository**: Your project should be in a Git repository
3. **Python Environment**: Python 3.9+ installed locally

## Required Files

Make sure you have these files in your project directory:

### Data Files (Required)
- `Books.csv` - Book information dataset
- `Users.csv` - User information dataset  
- `Ratings.csv` - User ratings dataset

### Model Files (Will be generated)
- `popular.pkl` - Popularity-based recommendations
- `pt.pkl` - Pivot table for collaborative filtering
- `books.pkl` - Processed books data
- `similarity_scores.pkl` - Similarity matrix

### Application Files (Created)
- `app.py` - Flask web application
- `requirements.txt` - Python dependencies
- `Procfile` - Railway deployment configuration
- `runtime.txt` - Python version specification
- `generate_models.py` - Script to create model files

## Step 1: Generate Model Files

Before deploying, you need to generate the pickle files that contain the trained models:

```bash
python generate_models.py
```

This script will:
- Load your CSV datasets
- Generate popularity-based recommendations
- Create collaborative filtering models
- Save everything to pickle files

**Important**: Make sure your CSV files are in the same directory when running this script.

## Step 2: Deploy to Railway

### Option A: Deploy via Railway Dashboard

1. **Connect Repository**:
   - Go to [railway.app](https://railway.app)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

2. **Configure Project**:
   - Railway will automatically detect it's a Python project
   - The `Procfile` tells Railway to run `gunicorn app:app`
   - The `runtime.txt` specifies Python 3.9.18

3. **Deploy**:
   - Railway will install dependencies from `requirements.txt`
   - Build and deploy your application
   - Provide you with a public URL

### Option B: Deploy via Railway CLI

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login and Deploy**:
   ```bash
   railway login
   railway init
   railway up
   ```

## Step 3: Verify Deployment

Once deployed, your API will be available at the Railway-provided URL. Test these endpoints:

- **Home**: `https://your-app.railway.app/`
- **Health Check**: `https://your-app.railway.app/health`
- **Popular Books**: `https://your-app.railway.app/popular`
- **Recommendations**: `https://your-app.railway.app/recommend/1984`
- **Search**: `https://your-app.railway.app/search/harry`

## API Endpoints

### GET `/`
Returns API information and available endpoints.

### GET `/popular`
Returns top 50 popular books with ratings and image URLs.

### GET `/recommend/<book_name>`
Returns book recommendations based on a specific book title.

### GET `/search/<query>`
Searches for books by title or author.

### GET `/health`
Health check endpoint for monitoring.

## Troubleshooting

### Common Issues

1. **Models Not Loaded**:
   - Ensure you ran `generate_models.py` before deployment
   - Check that all pickle files are committed to your repository

2. **Missing Dependencies**:
   - Verify `requirements.txt` contains all necessary packages
   - Check Railway build logs for installation errors

3. **Port Issues**:
   - The app automatically uses Railway's `PORT` environment variable
   - No manual port configuration needed

4. **Memory Issues**:
   - Large datasets might cause memory problems
   - Consider using Railway's higher-tier plans for more memory

### Monitoring

- Use Railway's built-in monitoring dashboard
- Check the `/health` endpoint regularly
- Monitor application logs in Railway dashboard

## File Structure After Deployment

```
your-project/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── Procfile             # Railway deployment config
├── runtime.txt          # Python version
├── generate_models.py   # Model generation script
├── Books.csv            # Book dataset
├── Users.csv            # User dataset
├── Ratings.csv          # Ratings dataset
├── popular.pkl          # Generated model file
├── pt.pkl              # Generated model file
├── books.pkl            # Generated model file
└── similarity_scores.pkl # Generated model file
```

## Next Steps

After successful deployment:

1. **Test all endpoints** to ensure they work correctly
2. **Set up monitoring** using Railway's dashboard
3. **Configure custom domain** if needed
4. **Set up CI/CD** for automatic deployments
5. **Monitor performance** and scale as needed

## Support

If you encounter issues:
1. Check Railway's build and runtime logs
2. Verify all required files are present
3. Ensure CSV files are properly formatted
4. Check that models were generated successfully

Your Book Recommender System should now be accessible via Railway's public URL! 🚀 