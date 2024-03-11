def create_quarterly_array() -> list:
    try:
        print(quarters)
    except UnboundLocalError:
        quarters = []
    
    return quarters

def add_data_to_quarterly_array(data: dict, quarters: list):
    for q in quarters:
        if q.get('quarter') == data.get('quarter'):
            for k, v in data.items():
                if k != 'quarter':
                    q[k] = v
            # exit if quarter was found
            break
        
    quarters.append(data)