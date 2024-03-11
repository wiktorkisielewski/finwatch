def enterprise_value(market_cap: float, debt: float, cash: float, cash_eq: float) -> float:
    ev = (market_cap + debt) - cash - cash_eq
    return ev

# EBIT / enterprise value.
def earnings_yeld(enterpise_value: float, ebit: float) -> float:
    earnings_yeld = ebit/enterpise_value
    return earnings_yeld

# EBIT / (net fixed assets + working capital)
# note: fixed assets = total_non_current_assets
def return_on_capital(current_assets: float, current_liabilities: float, ebit: float, total_non_current_assets: float) -> float:
    working_capital = current_assets - current_liabilities
    return_on_capital = ebit / (total_non_current_assets + working_capital)
    return return_on_capital