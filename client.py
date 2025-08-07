import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class GeminiBlogGenerator:
    def __init__(self):
        key = os.getenv("GEMINI_API_KEY")
        if not key:
            raise ValueError("API key not found")
        
        genai.configure(api_key=key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def system_prompt(self):
        return "You are the best surgeon and Medical doctor  in the world. Answer like a confident expert in medical science and keep answer brief but well formatted and like an experienced Doctor"

    def generate(self, user_prompt: str) -> str:
        # Create the model with system instruction
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=self.system_prompt()
        )
        
        # Generate content directly
        response = model.generate_content(user_prompt)
        return response.text
