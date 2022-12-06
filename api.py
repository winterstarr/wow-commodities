from collections import defaultdict

import pandas as pd
import requests
import weightedstats as ws

from oauth import get_new_api_key


def get_data():
    url = "https://us.api.blizzard.com/data/wow/auctions/commodities?namespace=dynamic-us&locale=en_US&access_token={}"
    try:
        token = load_token()
        response = requests.get(url.format(token))
        data = response.json()
    except:
        token = get_new_api_key()
        save_token(token)
        response = requests.get(url.format(token))
        data = response.json()

    price_data = combine_items(data['auctions'])
    df = pd.DataFrame.from_dict(price_data).T
    df.index.name = 'item_id'
    return df


def load_token():
    with open("token.txt") as f:
        return f.read()


def save_token(token):
    with open("token.txt", "w") as f:
        f.write(token)



def combine_items(data):
    items = defaultdict(lambda: defaultdict(int))
    for row in data:
        id = row['item']['id']
        price = row['unit_price']
        quantity = row['quantity']
        items[id][price] += quantity
    price_data = {}
    for id, item_dict in items.items():
        price_data[id] = get_stats(item_dict)
    return price_data


def get_stats(item_dict):
    k, v = zip(*item_dict.items())
    return dict(min_price=int(min(k) / 100),
                median=int(ws.weighted_median(k, v) / 100),
                quantity=int(sum(v)))
