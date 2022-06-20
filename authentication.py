import os

from dotenv import load_dotenv
load_dotenv(verbose=True) # Throws error if it can't find .env file

class Authentication:
    """
    Class to handle authentication for the Twitter API
    """

    def __init__(self):
        self.BEARER_TOKEN = os.getenv("bearer")
    
    def get_oauth2_bearer_token(self, r):
        
        r.headers["Authorization"] = f"Bearer {self.BEARER_TOKEN}"
        return r

