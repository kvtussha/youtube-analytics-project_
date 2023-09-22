import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
