import os

from backend.kaufland_app.routes.routes import get_products
from groq import Groq
from dotenv import load_dotenv

from backend.utils.pdf_processing import pdf_to_jpeg

load_dotenv()
groq = Groq(api_key=os.getenv('GROQ_API_KEY'))
pdf_path = "Kaufland-23-12-2024-24-12-2024-04.pdf"  # Path to your PDF file

results = get_products(pdf_path, groq)





