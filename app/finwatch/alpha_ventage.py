import requests
from auth import alpha_token

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=IBM&apikey={alpha_token}'
r = requests.get(url)
data = r.json()

print(data)