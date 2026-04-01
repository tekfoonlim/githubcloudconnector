
#For secure token handling
import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path(__file__).resolve().parent / "pat_token.env"
# print("Env Path",env_path)
load_dotenv(dotenv_path=env_path)

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
BASE_URL = "https://api.github.com"
