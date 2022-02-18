import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def point_percentage_chart():
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', 'PTS', '_3PM', 'FTM'])
    print(type(stats_df['_3PM']))

point_percentage_chart()