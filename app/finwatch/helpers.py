def create_quarterly_array() -> list:
    try:
        print(quarters)
    except UnboundLocalError:
        quarters = []
    
    return quarters

def add_data_to_quarterly_array(data: dict, quarters: list) -> list:
    found = False

    for q in quarters:
        if q.get('quarter') == data.get('quarter'):
            found = True
            for k, v in data.items():
                if k != 'quarter':
                    q[k] = v
            # exit if quarter was found
            break

    if not found:
        quarters.append(data)

    return quarters