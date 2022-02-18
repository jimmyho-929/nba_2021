import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def attempt_percentage_chart():
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', '_3PA', 'FGA'])

attempt_percentage_chart()