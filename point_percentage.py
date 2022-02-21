import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset with specific columns
stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', 'PTS', '_3PM', 'FTM', 'SEASON'])

# create series 
series_3PM = stats_df['_3PM']
series_FTM = stats_df['FTM']
series_PTS = stats_df['PTS']

# create new series with points scored from each category
stats_df = stats_df.assign(Pts_from_3 = series_3PM * 3, Pts_from_FT = series_FTM * 1)
stats_df = stats_df.assign(Pts_from_2 = series_PTS - stats_df['Pts_from_3'] - stats_df['Pts_from_FT'])

# create new series calculating point percentage
stats_df = stats_df.assign(PTSpct_from_3 = stats_df['Pts_from_3'] / series_PTS * 100)
stats_df = stats_df.assign(PTSpct_from_FT = stats_df['Pts_from_FT'] / series_PTS * 100)
stats_df = stats_df.assign(PTSpct_from_2 = stats_df['Pts_from_2'] / series_PTS * 100)

# calculate NBA mean percentage by season. Note: Totals do not add up to 100%; earlier seasons are under 100% and more recent seasons are over 100%
PTSpcnt_by_3_avg = stats_df.groupby('SEASON')['Pts_from_3'].aggregate(np.mean)
PTSpcnt_by_3_avg.name = 'By 3'
PTSpcnt_by_FT_avg = stats_df.groupby('SEASON')['Pts_from_FT'].aggregate(np.mean)
PTSpcnt_by_FT_avg.name = 'By FT'
PTSpcnt_by_2_avg = stats_df.groupby('SEASON')['Pts_from_2'].aggregate(np.mean)
PTSpcnt_by_2_avg.name = 'By 2'


df_avg = pd.concat([PTSpcnt_by_FT_avg, PTSpcnt_by_2_avg, PTSpcnt_by_3_avg], axis=1)
    
df_avg.plot.bar(title='NBA Mean Percentage Of Points Scored By Category')
plt.show()