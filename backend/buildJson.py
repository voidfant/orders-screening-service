import json


def build(data: list, internal: bool):
    new_data = []
    temp = {}

    for v in data:
        temp['order_id'] = v[0]
        temp['order_number'] = v[1]
        temp['cost_usd'] = v[2]
        temp['cost_rub'] = v[3]
        temp['order_date'] = v[4]
        new_data.append(temp.copy())
    
    # print(new_data)
    if internal:
        return new_data

    result = json.dumps(new_data)

    return result