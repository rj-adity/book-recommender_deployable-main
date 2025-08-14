#!/usr/bin/env python3
"""
Simple test script to verify the Flask API works correctly.
Run this after starting the Flask app locally.
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_endpoint(endpoint, description):
    """Test a specific API endpoint"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        print(f"\n🔍 Testing {description}:")
        print(f"   URL: {BASE_URL}{endpoint}")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Success: {data.get('message', 'No message')}")
            if 'count' in data:
                print(f"   📊 Count: {data['count']}")
        else:
            print(f"   ❌ Error: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print(f"\n❌ Connection Error: Make sure the Flask app is running on {BASE_URL}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")

def main():
    """Test all API endpoints"""
    print("🚀 Book Recommender API Test")
    print("=" * 40)
    print("Make sure the Flask app is running with: python app.py")
    print()
    
    # Test all endpoints
    test_endpoint("/", "Home endpoint")
    test_endpoint("/health", "Health check")
    test_endpoint("/popular", "Popular books")
    test_endpoint("/recommend/1984", "Book recommendations for '1984'")
    test_endpoint("/search/harry", "Search for 'harry'")
    
    print("\n" + "=" * 40)
    print("🎯 Test completed!")
    print("\nIf all tests pass, your API is ready for Railway deployment!")

if __name__ == "__main__":
    main() 