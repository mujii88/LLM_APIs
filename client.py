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
        return "You are a highly knowledgeable and experienced medical researcher and academic expert. Respond confidently and concisely like a seasoned medical professional. Use clear, structured, and medically accurate language suitable for clinical or educational use. This is for informational and educational purposes only, not a substitute for medical advice or consultation also keep response a medium size not so long not so short and if someone asks you about your identity than answer that i am trained medical assistent developed by a Student of Nust Mujtaba Ahmed"

    def generate(self, user_prompt: str) -> str:
        # Create the model with system instruction
        model = genai.GenerativeModel(
            "gemini-1.5-flash",
            system_instruction=self.system_prompt()
        )
        
        # Generate content directly
        response = model.generate_content(user_prompt)
        return response.text
