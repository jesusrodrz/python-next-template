from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Environment:
    DEBUG: bool= os.getenv('DEBUG', 'False').lower() == 'true'