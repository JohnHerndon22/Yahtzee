# report_results.py

import pandas as pd
import os

dfgameresults = pd.read_csv('game_results.csv')
os.system("clear")
        
print(dfgameresults.describe())
print(dfgameresults.columns)
total_games = len(dfgameresults.index)
print('number of games played: ', len(dfgameresults.index))
print('high score: ', str(dfgameresults['total_score'].max()))
print('low score: ', str(dfgameresults['total_score'].min()))
print('avg score: ', str(round(dfgameresults['total_score'].mean(),2)))
print(dfgameresults.loc[dfgameresults['full_house']==25])
df.loc[df['favorite_color'] == 'yellow']



