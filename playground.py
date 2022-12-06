from pathlib import Path

import pandas as pd

dfs = []
for file in Path("data").iterdir():
    df = pd.read_csv(file)
    df['date'] = file.name.split('.')[0]
    dfs.append(df)

df = pd.concat(dfs)
df['date'] = pd.to_datetime(df['date'], format="%y%m%d%H")

bars = {
    2840: "Copper Bar",
    3576: "Tin Bar",
    2841: "Bronze Bar",
    2842: "Silver Bar",
    3575: "Iron Bar",
    3577: "Gold Bar",
    3859: "Steel Bar",
    3858: "Mithril Bar",
    6037: "Truesilver Bar",
    3860: "Mithril Bar",
    12359: "Thorium Bar",
    12655: "Enchanted Thorium Bar",
    12360: "Arcanite Bar",
    11371: "Dark Iron Bar",
}

df[df.item_id == 2840].set_index('date').min_price.plot()
print(df)