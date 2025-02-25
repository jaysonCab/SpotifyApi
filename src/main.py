# Loads all environmental variables specifically from .env file
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(f'{client_id}, {client_secret}')