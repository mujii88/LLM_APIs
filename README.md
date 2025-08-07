# 🏥 AI Medical Assistant

A FastAPI backend with an interactive frontend for medical consultations using Google's Gemini AI.

## 🚀 Features

- **AI Medical Assistant**: Powered by Google Gemini API
- **Interactive Frontend**: Beautiful animations and responsive design
- **Real-time Responses**: Instant medical advice and consultations
- **Secure API**: Environment-based configuration

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key
- Git

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd appAPI
```

### 2. Create Virtual Environment
```bash
python -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```bash
# Gemini API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Server Configuration (Optional)
HOST=0.0.0.0
PORT=8000
```

**⚠️ Important**: Never commit your `.env` file to Git!

### 5. Get Your Gemini API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## 🚀 Running Locally

### Start the Backend
```bash
# Activate virtual environment
source myvenv/bin/activate

# Run FastAPI server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Start the Frontend
```bash
# Serve the HTML file
python -m http.server 3001
```

### Access the Application
- **Frontend**: http://localhost:3001/frontend.html
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🌐 Deployment Options

### Option 1: Railway (Recommended)
1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Deploy**:
   ```bash
   railway init
   railway up
   ```

4. **Set Environment Variables**:
   - Go to Railway Dashboard
   - Add `GEMINI_API_KEY` variable

### Option 2: Render
1. **Connect your GitHub repo**
2. **Create a new Web Service**
3. **Configure**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**: Add `GEMINI_API_KEY`

### Option 3: Heroku
1. **Install Heroku CLI**
2. **Create Procfile**:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
3. **Deploy**:
   ```bash
   heroku create your-app-name
   heroku config:set GEMINI_API_KEY=your_key_here
   git push heroku main
   ```

### Option 4: Vercel
1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Create vercel.json**:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "main.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "main.py"
       }
     ]
   }
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```

## 🔒 Security Best Practices

### ✅ Do's
- ✅ Use environment variables for API keys
- ✅ Add `.env` to `.gitignore`
- ✅ Use HTTPS in production
- ✅ Validate all inputs
- ✅ Rate limit API endpoints

### ❌ Don'ts
- ❌ Never commit API keys to Git
- ❌ Don't expose sensitive data in logs
- ❌ Don't use hardcoded credentials

## 📁 Project Structure
```
appAPI/
├── main.py              # FastAPI application
├── client.py            # Gemini API client
├── frontend.html        # Interactive frontend
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in Git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 API Endpoints

- `GET /` - Health check
- `POST /generate` - Generate AI response
- `GET /docs` - Interactive API documentation

## 🐛 Troubleshooting

### Common Issues

1. **"API key not found"**
   - Check your `.env` file exists
   - Verify `GEMINI_API_KEY` is set correctly

2. **"Failed to fetch"**
   - Ensure backend is running on port 8000
   - Check CORS configuration

3. **"Module not found"**
   - Activate virtual environment
   - Install dependencies: `pip install -r requirements.txt`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section
2. Review the API documentation
3. Create an issue on GitHub

---

**Made with ❤️ using FastAPI and Google Gemini AI**
