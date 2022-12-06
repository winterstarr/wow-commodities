import datetime


def save_data(data):
    time = get_timestamp()
    data.to_csv(f'./data/{time}.csv')


def get_timestamp():
    time = datetime.datetime.now()
    return time.strftime('%y%m%d%H')