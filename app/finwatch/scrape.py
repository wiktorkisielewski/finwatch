import alpha_ventage as av
import psql as psql

stocks = av.get_active_tickers(active_listings=av.list_active_tickers(), stocks=True, etfs=False)
etfs = av.get_active_tickers(active_listings=av.list_active_tickers(), stocks=False, etfs=True)

print(tickers)

def main():
    psql.init_databases(['stocks', 'etfs'])
