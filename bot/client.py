from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    return Client(
        api_key=os.getenv('BINANCE_KEY'),
        api_secret=os.getenv('BINANCE_SECRET'),
        testnet=True
    )

