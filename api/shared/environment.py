from dotenv import load_dotenv
import os


# Load environment variables from the .env file
load_dotenv()


class Environment:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
