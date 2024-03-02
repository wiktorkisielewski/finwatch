import finnhub
import os

finnhub_client = finnhub.Client(api_key=os.environ.get("FINHUB_API_KEY"))
