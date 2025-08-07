
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from client import GeminiBlogGenerator
from fastapi.middleware.cors import CORSMiddleware

class PromptRequest(BaseModel):
    user_prompt: str

app = FastAPI()

# Add CORS middleware with proper configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Hello from FastAPI!"})

@app.post("/generate")
async def generate(request: PromptRequest):
    try:
        generator = GeminiBlogGenerator()
        response_text = generator.generate(request.user_prompt)
        return JSONResponse(content={"response": response_text})
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)