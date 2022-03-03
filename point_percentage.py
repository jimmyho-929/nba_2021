import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import dataset with specific columns
stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv', usecols=['TEAM', 'PTS', '_3PM', 'FTM', 'SEASON'])

# create series 
series_3PM = stats_df['_3PM']
series_FTM = stats_df['FTM']
series_PTS = stats_df['PTS']

# create new series after calculating points scored from each category and adds to dataframe
stats_df = stats_df.assign(Pts_from_3 = series_3PM * 3, Pts_from_FT = series_FTM * 1)
stats_df = stats_df.assign(Pts_from_2 = series_PTS - stats_df['Pts_from_3'] - stats_df['Pts_from_FT'])

# create new series calculating point percentage and adds to dataframe
def percentage(category):
    ''' 
        Formula: Point category / Total team points per game * 100 = Point percentage

        Parameter:
            category (string): Series from dataframe

        Return:
            Returns a decimal outputting the point percentage and adds to the dataframe
    '''
    return stats_df[category] / series_PTS * 100

stats_df = stats_df.assign(PTSpct_from_3 = percentage('Pts_from_3'))
stats_df = stats_df.assign(PTSpct_from_FT = percentage('Pts_from_FT'))
stats_df = stats_df.assign(PTSpct_from_2 = percentage('Pts_from_2'))


def szn_avg_df(series):
    '''
        used for shorthanding code

        Parameter:
            series (string): Series from dataframe

        Return:
            Returns the mean point percentage category by season and adds to the dataframe
    '''
    return stats_df.groupby('SEASON')[series].aggregate(np.mean)

# calculate NBA mean percentage by season. NOTE: Totals do not add up to 100%; earlier seasons are under 100% and more recent seasons are over 100%
PTSpcnt_by_3_avg = szn_avg_df('Pts_from_3')
PTSpcnt_by_FT_avg = szn_avg_df('Pts_from_FT')
PTSpcnt_by_2_avg = szn_avg_df('Pts_from_2')

# renaming category
PTSpcnt_by_FT_avg.name = 'By FT'
PTSpcnt_by_3_avg.name = 'By 3'
PTSpcnt_by_2_avg.name = 'By 2'

df_avg = pd.concat([PTSpcnt_by_FT_avg, PTSpcnt_by_2_avg, PTSpcnt_by_3_avg], axis=1)
    
df_avg.plot.bar(stacked=True, title='NBA Mean Percentage Of Points Scored By Category').legend(loc='best',bbox_to_anchor=(1.0, 0.5))
plt.show()