import pandas as pd

stats = pd.read_csv('dataset/nba_team_stats_00_to_21.csv')
print(pd.DataFrame(stats, columns=['WIN%','FGA','FGM','3PA','3PM','SEASON']))
