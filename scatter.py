import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def scatter_chart():
    stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv')

    df_3PAavg = stats_df.groupby('SEASON')['_3PA'].aggregate(np.mean)
    df_3PA = pd.DataFrame(df_3PAavg)
    df_3PA.reset_index(inplace=True)
    df_3PA.columns=['SEASON', '3PA']
    # print(type(df_3PA))
    df_3PA.plot(x='SEASON', y='3PA', kind='scatter', rot=45, title='NBA Mean 3pt Attempts By Season')
    plt.show()