#test_yahtzee.py

import pandas as pd
from common import *

#setup for test - expect failure
test = 'small straight test bad->'
currentTurn = [[3, True], [3, False], [4, True], [5, True], [3, False]]
dfrolls = pd.DataFrame(currentTurn,columns=['roll','holder'])
selection = 10
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dfrolls, currentTurn)==False:
    print(test,'passed')
else:
    print(test,'failed')


# setup for test - expect pass
test = 'small straight test good->'
currentTurn = [[1, True], [2, False], [3, True], [4, True], [1, False]]
dfrolls = pd.DataFrame(currentTurn,columns=['roll','holder'])
selection = 10
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dfrolls, currentTurn)==True:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'large straight test bad->'
currentTurn = [[3, True], [3, False], [4, True], [5, True], [3, False]]
dfrolls = pd.DataFrame(currentTurn,columns=['roll','holder'])
selection = 10
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dfrolls, currentTurn)==False:
    print(test,'passed')
else:
    print(test,'failed')


# setup for test - expect pass
test = 'large straight test good->'
currentTurn = [[1, True], [2, False], [3, True], [4, True], [5, False]]
dfrolls = pd.DataFrame(currentTurn,columns=['roll','holder'])
selection = 11
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dfrolls, currentTurn)==True:
    print(test,'passed')
else:
    print(test,'failed')


# test roll window
dice = [[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),True],[random.randint(1,6),False],[random.randint(1,6),True]]   
dicelayout = refresh_dice_table(dice)
window = sg.Window('Test Window', dicelayout).Finalize()
event, values = window.read()
print(event)
print(values)