from os import stat
import pandas as pd
from pandasql import sqldf
import numpy as np
from sqlalchemy import true
import matplotlib.pyplot as plt

pysqldf = lambda q: sqldf(q, globals())

stats = pd.read_csv('dataset/nba_team_stats_00_to_21.csv')
#print(pandas.DataFrame(stats, columns=['_3PA','TEAM', 'SEASON']))
#print(stats[['_3PA','TEAM']])
#print(stats[(stats['SEASON']=='2000-01')]['_3PA'])
_20003PAavg = stats.groupby('SEASON')['_3PA'].aggregate(np.mean)
df_3PA = pd.DataFrame(_20003PAavg)
df_3PA.reset_index(inplace=True)
df_3PA.columns=['SEASON', '3PA']
print(df_3PA)
df_3PA.plot(x='SEASON', y='3PA', kind='scatter')
plt.show()


q = """SELECT AVG(_3PA)
        FROM stats
        WHERE SEASON='2000-01' 
        """

_20003PA = pysqldf(q)
#
#print('2000-01 NBA 3 Point Attempt Average:',float(_20003PA.values))
