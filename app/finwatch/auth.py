import finnhub
import os

token = os.environ.get("FINHUB_API_KEY")
alpha_token = os.environ.get("ALPHA_KEY")
finnhub_client = finnhub.Client(api_key=token)
