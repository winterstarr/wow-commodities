import pandas as pd

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

ores = {
    2770: "Copper Ore",
    2771: "Tin Ore",
    2775: "Silver Ore",
    2772: "Iron Ore",
    2776: "Gold Ore",
    3858: "Mithril Ore",
    7911: "Truesilver Ore",
    11370: "Dark Iron Ore",
    10620: "Thorium Ore",
}
print(pd.read_csv('data/22113021.csv').set_index('item_id').loc[2840])
df = pd.read_csv('data/22113021.csv').set_index('item_id')

for bar, name in bars.items():
    print(name, df.loc[bar]['min_price']/100)
