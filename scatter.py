import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ✅ Category 2: Utilize External Data 
# Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

stats_df = pd.read_csv('dataset/nba_team_stats_00_to_21.csv')

# create Series that shows average 3pt attempt by season as a whole
df_3PAavg = stats_df.groupby('SEASON')['_3PA'].aggregate(np.mean)

# Category 3: Data Display
# ✅: Visualize data in a graph, chart, or other visual representation of data.

# create new dataframe with calculated averages
df_3PA = pd.DataFrame(df_3PAavg)
df_3PA.reset_index(inplace=True)
df_3PA.columns=['SEASON', '3PA']
df_3PA.plot(x='SEASON', y='3PA', kind='scatter', rot=45, title='NBA Mean 3pt Attempts By Season')
plt.show()