import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def attempt_percentage_chart():
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', '_3PA', 'FGA', 'SEASON'])
    
    series_3PA = stats_df['_3PA']
    series_FGA = stats_df['FGA']

    stats_df = stats_df.assign(Threes_Att_Pcnt = (series_3PA / series_FGA) * 100)
    stats_df = stats_df.assign(Twos_Att_Pcnt = 100 - stats_df['Threes_Att_Pcnt'])

    df_shot_attempts = stats_df.loc[stats_df['SEASON'] == '2020-21', :]
    df_shot_attempts = pd.DataFrame(df_shot_attempts, columns=['TEAM', 'Threes_Att_Pcnt', 'Twos_Att_Pcnt'])

    df_shot_attempts.plot.bar(x='TEAM', stacked=True, title='3pt Attempts Vs. 2pt Attempts 2021-22 Season')
    plt.show()