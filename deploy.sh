#!/bin/bash

echo "🚀 AI Medical Assistant Deployment Script"
echo "========================================"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ Error: .env file not found!"
    echo "Please create a .env file with your GEMINI_API_KEY"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "myvenv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv myvenv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source myvenv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if all required files exist
echo "✅ Checking project files..."
required_files=("main.py" "client.py" "frontend.html" "requirements.txt")
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Error: $file not found!"
        exit 1
    fi
done

echo "✅ All files present!"

# Start the application
echo "🚀 Starting FastAPI server..."
echo "📍 Backend: http://localhost:8000"
echo "📍 Frontend: http://localhost:3001/frontend.html"
echo "📍 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop the server"

# Start the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000 