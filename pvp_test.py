"""Converts pvp.json file into dictionary using json module"""
import json

with open('pvp.json') as f:
    pvp = json.load(f)

print(pvp)

