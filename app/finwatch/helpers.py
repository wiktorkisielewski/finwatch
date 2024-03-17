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
    result = []

    for line in lines[1:]:
        values = line.split(",")
        entry = {}
        for i in range(len(header)):
            entry[header[i]] = values[i]
        result.append(entry)

    print(result)
