import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set")

if not PINECONE_API_KEY:
    raise RuntimeError("PINECONE_API_KEY is not set")