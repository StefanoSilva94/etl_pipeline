"""
Initial file to explore the data set
"""

import pandas as pd

data = pd.read_csv('data/raw/fb_ref_players_2023_2024.csv')

print(data.head())

print(data.columns)

# print(data.info())
