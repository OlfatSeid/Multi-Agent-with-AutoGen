

import os
from dotenv import load_dotenv, find_dotenv

                                                                                                                   # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_groq_api_key():
    load_env()
    groq_api_key = os.getenv("GROQ_API_KEY")
    return groq_api_key
