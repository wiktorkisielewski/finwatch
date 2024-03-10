# from finwatch.auth import finnhub_client
from auth import finnhub_client, token
import requests


def get_basic_financials(ticker: str):
    basic_financials = finnhub_client.company_basic_financials(ticker, 'all')

    all_metrics = basic_financials['metric']
    single_metrics = []
    periodic_metrics = []

    metrics_with_periods = {}
    for metric_name, metric_value in all_metrics.items():
        periods = []

        if metric_name in basic_financials['series']['annual']:
            periods += basic_financials['series']['annual'][metric_name]
        elif metric_name in basic_financials['series']['quarterly']:
            periods += basic_financials['series']['quarterly'][metric_name]

        metrics_with_periods[metric_name] = {'values': metric_value, 'periods': periods}

    for metric_name, metric_data in metrics_with_periods.items():
        if len(metric_data['periods']) > 0:
            periodic_metrics.append(f"{metric_name}: {metric_data['values']} -> {metric_data['periods']}")
        else:
            single_metrics.append(f"{metric_name}: {metric_data['values']}")

    return single_metrics, periodic_metrics

def get_financials_as_reported(ticker: str):
    financials_as_reported = finnhub_client.financials_reported(symbol=ticker, freq='quarterly')

    symbol = financials_as_reported['symbol']
    latest_quarter_data = financials_as_reported['data'][0]  # Assuming the most recent quarter is at index 0

    # Iterate through the list and find the dictionary with 'concept' equal to 'us-gaap_Assets'
    assets_data = next(item for item in latest_quarter_data['report']['bs'] if item['concept'] == 'us-gaap_Assets')
    assets = assets_data['value']

    liabilities_data = next(item for item in latest_quarter_data['report']['bs'] if item['concept'] == 'us-gaap_Liabilities')
    liabilities = liabilities_data['value']
    
    year = latest_quarter_data['year']
    quarter = latest_quarter_data['quarter']

    print(f'TICKER: {symbol}\nY: {year} Q: {quarter}\nAssets:{assets}\nLiabilities{liabilities}')

def get_financials_as_reported_rest(ticker: str):
    url = "https://finnhub.io/api/v1/stock/financials-reported"
    params = {'symbol': 'AAPL', 'token': token}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}, {response.text}")

print(get_financials_as_reported_rest('AAPL'))