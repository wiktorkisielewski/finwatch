from auth import finnhub_client

basic_financials = finnhub_client.company_basic_financials('AAPL', 'all')

all_metrics = basic_financials['metric']

metrics_with_periods = {}
for metric_name, metric_value in all_metrics.items():
    periods = []

    if metric_name in basic_financials['series']['annual']:
        periods += basic_financials['series']['annual'][metric_name]
    elif metric_name in basic_financials['series']['quarterly']:
        periods += basic_financials['series']['quarterly'][metric_name]

    metrics_with_periods[metric_name] = {'values': metric_value, 'periods': periods}

for metric_name, metric_data in metrics_with_periods.items():
    print(f"{metric_name}: {metric_data['values']} with periods {metric_data['periods']}")
