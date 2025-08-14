#!/usr/bin/env python3
"""
Script to help deploy the Book Recommender System to Hugging Face Spaces.
This script will prepare your files and provide deployment instructions.
"""

import os
import shutil
import zipfile

def create_deployment_package():
    """Create a deployment package for Hugging Face Spaces"""
    
    print("🚀 Preparing Hugging Face Spaces Deployment Package")
    print("=" * 60)
    
    # Required files for Hugging Face Spaces
    required_files = [
        'app.py',                    # Flask API
        'gradio_app.py',            # Gradio interface
        'requirements.txt',          # Dependencies
        'README.md',                # Project description
        'Books.csv',                # Book dataset
        'Users.csv',                # User dataset
        'Ratings.csv',              # Ratings dataset
        'popular.pkl',              # Popularity model
        'pt.pkl',                   # Pivot table model
        'books.pkl',                # Books data model
        'similarity_scores.pkl'     # Similarity matrix
    ]
    
    # Check which files exist
    existing_files = []
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            existing_files.append(file)
        else:
            missing_files.append(file)
    
    print(f"✅ Found {len(existing_files)} files:")
    for file in existing_files:
        print(f"   - {file}")
    
    if missing_files:
        print(f"\n❌ Missing {len(missing_files)} files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all required files are present before deployment.")
        return False
    
    # Create deployment directory
    deploy_dir = "huggingface_deployment"
    if os.path.exists(deploy_dir):
        shutil.rmtree(deploy_dir)
    os.makedirs(deploy_dir)
    
    # Copy files to deployment directory
    print(f"\n📁 Creating deployment directory: {deploy_dir}")
    for file in existing_files:
        shutil.copy2(file, deploy_dir)
        print(f"   - Copied {file}")
    
    # Create deployment instructions
    instructions = """# 🚀 Hugging Face Spaces Deployment Instructions

## 📋 Steps to Deploy

### 1. Go to Hugging Face Spaces
- Visit: https://huggingface.co/spaces
- Click "Create new Space"

### 2. Configure Your Space
- **Owner**: Your username
- **Space name**: book-recommender-system (or your preferred name)
- **License**: Choose appropriate license
- **Space SDK**: Select "Gradio"
- **Space hardware**: Choose "CPU" (free tier)

### 3. Upload Files
- Choose "Upload files" option
- Upload ALL files from this deployment package
- Make sure to include the .pkl files (they're large!)

### 4. Wait for Build
- Hugging Face will automatically build your Space
- This usually takes 2-5 minutes
- Check build logs for any errors

### 5. Your Space is Live!
- Visit: https://huggingface.co/spaces/YOUR_USERNAME/book-recommender-system
- Test all features
- Share with others!

## 🔧 Important Notes

- **File Sizes**: The .pkl files are large (several MB each)
- **Build Time**: First build may take longer due to model loading
- **API Access**: Your Flask API will be available at the Space URL
- **Gradio Interface**: User-friendly interface for testing

## 🎯 Testing Your Deployment

1. **Health Check**: Verify system status
2. **Popular Books**: Test popularity recommendations
3. **Recommendations**: Try getting book suggestions
4. **Search**: Test book search functionality

## 🆘 Troubleshooting

- **Build Fails**: Check requirements.txt compatibility
- **Models Not Loading**: Verify all .pkl files are uploaded
- **API Errors**: Check build logs for specific issues

Good luck with your deployment! 🎉
"""
    
    with open(os.path.join(deploy_dir, "DEPLOYMENT_INSTRUCTIONS.md"), "w", encoding='utf-8') as f:
        f.write(instructions)
    
    # Create ZIP file for easy upload
    zip_filename = "book-recommender-huggingface.zip"
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in existing_files:
            zipf.write(file, file)
        zipf.write(os.path.join(deploy_dir, "DEPLOYMENT_INSTRUCTIONS.md"), "DEPLOYMENT_INSTRUCTIONS.md")
    
    print(f"\n📦 Created deployment package: {zip_filename}")
    print(f"📁 Deployment files are in: {deploy_dir}/")
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS:")
    print("1. Go to https://huggingface.co/spaces")
    print("2. Create a new Space")
    print("3. Upload the files from the deployment directory")
    print("4. Wait for build to complete")
    print("5. Your API will be live!")
    print("=" * 60)
    
    return True

def main():
    """Main deployment preparation function"""
    print("📚 Book Recommender System - Hugging Face Deployment")
    print("=" * 60)
    
    success = create_deployment_package()
    
    if success:
        print("\n✅ Deployment package created successfully!")
        print("📖 Check DEPLOYMENT_INSTRUCTIONS.md for detailed steps")
    else:
        print("\n❌ Failed to create deployment package")
        print("Please fix the missing files and try again")

if __name__ == "__main__":
    main() 