from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv(dotenv_path=".secrets")

# Access the API key
API_KEY = os.getenv("API_KEY")
