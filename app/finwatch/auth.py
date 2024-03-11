import finnhub
import os

# ALPHA VENTAGE
alpha_token = os.environ.get("ALPHA_KEY")

# FINHUB
token = os.environ.get("FINHUB_API_KEY")
finnhub_client = finnhub.Client(api_key=token)
