# Enterprise value =
# common equity at market value (this line item is also known as "market cap")
# + debt at market value (here debt refers to interest-bearing liabilities, both long-term and short-term)
# + preferred equity at market value
# + unfunded pension liabilities and other debt-deemed provisions
# – value of associate companies
# – cash and cash equivalents.

# sum of market cap and debt minus cash and cash equivalents.


def calc_enterprise_value(market_cap: float, debt: float, cash: float, cash_eq: float) -> float:
    ev = (market_cap + debt) - cash - cash_eq
    return ev
