import alpha_ventage as av 
from helpers import get_latest_quarter

def screen_stocks(stocks_list: list) -> list:
    x = 0 

    for stock in stocks_list:
        if x >=10:
            break
        else:
            # to do - magic_fromula only for last quarter
            stock_magic_data = av.magic_formula(ticker=stock)
            print(stock, get_latest_quarter(stock_magic_data))


        x += 1

def main():
    # stocks_list = av.get_active_tickers(active_listings=av.list_active_tickers(), stocks=True, etfs=False)

    # tmp
    stocks_list = ["AAPL", "IBM", "MSFT", "TTWO"]

    screen_stocks(stocks_list=stocks_list)

main()