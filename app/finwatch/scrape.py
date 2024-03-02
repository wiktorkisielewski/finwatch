from finwatch.auth import finnhub_client

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