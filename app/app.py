from dotenv import load_dotenv
from fastapi import FastAPI
import os
from supabase import create_client, Client

load_dotenv()
app = FastAPI()

# Initialize Supabase client
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)
