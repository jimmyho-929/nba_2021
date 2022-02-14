import pandas
from pandasql import sqldf

pysqldf = lambda q: sqldf(q, globals())

stats = pandas.read_csv('dataset/nba_team_stats_00_to_21.csv')

q = """SELECT AVG(_3PA)
        FROM stats
        WHERE SEASON='2000-01' 
        """

_20003PA = pysqldf(q)
print('2000-01 NBA 3 Point Attempt Average:',float(_20003PA.values))
