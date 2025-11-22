import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

for model in genai.list_models():
    print(f"Nome: {model.name}")
    print(
        f"Suporta geração de conteúdo? {'generateContent' in model.supported_generation_methods}"
    )
    print("-" * 40)
