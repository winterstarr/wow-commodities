import pandas as pd

class Ledger:
    def __init__(self, filename):
        self.df = None
        self.filename = filename
        self.load()

    def load(self):
        self.df = pd.read_csv(self.filename).set_index('date')

    def save(self):
        self.df.to_csv(self.filename)

    def buy(self, item, quantity, price):
        pass

