def create_quarterly_array() -> list:
    try:
        print(quarters)
    except UnboundLocalError:
        quarters = []

    return quarters


def add_data_to_quarterly_array(data: dict, quarters: list) -> list:
    found = False

    for q in quarters:
        if q.get("quarter") == data.get("quarter"):
            found = True
            for k, v in data.items():
                if k != "quarter":
                    q[k] = v
            # exit if quarter was found
            break

    if not found:
        quarters.append(data)

    return quarters


def get_active_tickers(active_listings: str, stocks: bool, etfs: bool) -> list:
    lines = active_listings.strip().split("\n")
    header = lines[0].split(",")
    tickers_list = []

    for line in lines[1:]:
        values = line.split(",")
        if values[-1] == "Active":
            entry = {}
            for i in range(len(header)):
                entry[header[i]] = values[i]
            tickers_list.append(entry)


    # stocks & etf filter
    new_tickers_list = []
    x = 0 
    max_x = len(tickers_list)

    print(x, max_x)

    while x < max_x:
        # print(tickers_list[x])
        ticker_data = tickers_list[x]
        if stocks is True:
            if ticker_data["assetType"] == "Stock":
                new_tickers_list.append(tickers_list[x])
        if etfs is True:
            if ticker_data["assetType"] == "ETF":
                new_tickers_list.append(tickers_list[x])
        x += 1

    tickers_list = new_tickers_list
    
    return tickers_list
