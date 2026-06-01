import os
import time

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    secret_key = os.getenv("BINANCE_API_SECRET")

    if not api_key or not secret_key:
        raise ValueError("Missing API Credentials in .env file.")
    
    client = Client(api_key, secret_key, testnet=True)

    client.timestamp_offset = (
        client.get_server_time()['serverTime'] 
        - int(time.time()*1000)
    )

    return client