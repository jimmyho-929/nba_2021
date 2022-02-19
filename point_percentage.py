import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def point_percentage_chart():
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', 'PTS', '_3PM', 'FTM', 'SEASON'])
    series_3PM = stats_df['_3PM']
    series_FTM = stats_df['FTM']
    series_PTS = stats_df['PTS']
    stats_df = stats_df.assign(Pts_from_3 = series_3PM * 3, Pts_from_FT = series_FTM * 1)
    stats_df = stats_df.assign(Pts_from_2 = series_PTS - stats_df['Pts_from_3'] - stats_df['Pts_from_FT'])
    stats_df = stats_df.assign(PTSpct_from_3 = stats_df['Pts_from_3'] / series_PTS * 100)
    stats_df = stats_df.assign(PTSpct_from_FT = stats_df['Pts_from_FT'] / series_PTS * 100)
    stats_df = stats_df.assign(PTSpct_from_2 = stats_df['Pts_from_2'] / series_PTS * 100)

    PTSpcnt_by_3_avg = stats_df.groupby('SEASON')['Pts_from_3'].aggregate(np.mean)
    PTSpcnt_by_3_avg.name = 'Pt%_by_3'
    PTSpcnt_by_FT_avg = stats_df.groupby('SEASON')['Pts_from_FT'].aggregate(np.mean)
    PTSpcnt_by_FT_avg.name = 'Pt%_by_FT'
    PTSpcnt_by_2_avg = stats_df.groupby('SEASON')['Pts_from_2'].aggregate(np.mean)
    PTSpcnt_by_2_avg.name = 'Pt%_by_2'

    df_avg = pd.concat([PTSpcnt_by_FT_avg, PTSpcnt_by_2_avg, PTSpcnt_by_3_avg], axis=1)
    
    df_avg.plot.bar()
    plt.show()