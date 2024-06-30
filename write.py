import datetime
from pathlib import Path


def save_data(data):
    time = get_timestamp()
    data.to_csv(f'./data/{time}.csv')
    update(data, time)


def get_timestamp():
    time = datetime.datetime.now()
    return time.strftime('%y%m%d%H')

def update(data, time):
    out_dir = Path('item_data')
    for item_id, row in data.iterrows():
        csv_row = f'{time},{row["min_price"]},{row["median"]},{row["quantity"]}\n'
        with open(out_dir / f'{item_id}.csv', 'a') as f:
            f.write(csv_row)
