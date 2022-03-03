import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

season = input('From the 2000 to 2021 season, which season would you like to see the percentage of 3pt attempts compared to total shot attempts? (ex: 2000-01) ')
pattern = re.compile('^20[0-2][0-9]\-[0-2][0-9]')

if season == '2020-21':
    print('The data from this season is missing. Try a different season.')
    
elif pattern.match(season):
    # import dataset with specific columns
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', '_3PA', 'FGA', 'SEASON'])

    # select series
    series_3PA = stats_df['_3PA']
    series_FGA = stats_df['FGA']

    # create new series and add to dataframe
    stats_df = stats_df.assign(Threes_Att_Pcnt = (series_3PA / series_FGA) * 100)
    stats_df = stats_df.assign(Twos_Att_Pcnt = 100 - stats_df['Threes_Att_Pcnt'])

    # filter dataframe by user input
    df_shot_attempts = stats_df.loc[stats_df['SEASON'] == season, :]

    # create new dataframe 
    df_shot_attempts = pd.DataFrame(df_shot_attempts, columns=['TEAM', 'Threes_Att_Pcnt', 'Twos_Att_Pcnt'])

    df_shot_attempts.plot.bar(x='TEAM', stacked=True, title=f'3pt Attempts Vs. 2pt Attempts {season} Season')
    plt.show()
    
else:
    print(f'{season} was entered incorrectly. Try again. (ex: 2000-01)')



