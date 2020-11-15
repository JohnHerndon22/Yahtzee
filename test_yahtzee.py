#test_yahtzee.py

import pandas as pd
from common import *

#setup for test - expect failure
test = 'small straight test bad->'
dice = [[3, True], [3, False], [4, True], [5, True], [3, False]]
dfrolls = count_all_rolls(dice)
selection = 10
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


# setup for test - expect pass
test = 'small straight test good->'
dice = [[5, True], [2, False], [3, True], [4, True], [6, False]]
dfrolls = count_all_rolls(dice)
selection = 10
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==30:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'large straight test bad->'
dice = [[3, True], [3, False], [4, True], [5, True], [3, False]]
dfrolls = count_all_rolls(dice)
selection = 11
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


# setup for test - expect pass
test = 'large straight test good->'
dice = [[1, True], [2, False], [3, True], [4, True], [5, False]]
dfrolls = count_all_rolls(dice)
selection = 11
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==40:
    print(test,'passed')
else:
    print(test,'failed')

#  setup for test full house - expect pass
test = 'full house test bad->'
dice = [[1, True], [2, False], [1, True], [2, True], [5, False]]
dfrolls = count_all_rolls(dice)
selection = 9
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test full house - expect pass
test = 'full house test good'
dice = [[1, True], [1, False], [3, True], [3, True], [1, False]]
dfrolls = count_all_rolls(dice)
selection = 9
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==25:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test 3x kind - expect pass
test = 'three kind test bad->'
dice = [[1, True], [2, False], [1, True], [2, True], [5, False]]
dfrolls = count_all_rolls(dice)
selection = 7
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test full house - expect pass
test = 'three kind test good'
dice = [[1, True], [1, False], [3, True], [3, True], [1, False]]
dfrolls = count_all_rolls(dice)
selection = 7
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==9:
    print(test,'passed')
else:
    print(test,'failed')

#  setup for test 4x kind - expect pass
test = 'four kind test bad->'
dice = [[1, True], [2, False], [1, True], [2, True], [5, False]]
dfrolls = count_all_rolls(dice)
selection = 8
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test 4 x expect pass
test = 'four kind test good'
dice = [[1, True], [1, False], [3, True], [1, True], [1, False]]
dfrolls = count_all_rolls(dice)
selection = 8
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==7:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test 4x kind - expect pass
test = 'yah test bad->'
dice = [[1, True], [2, False], [1, True], [2, True], [5, False]]
dfrolls = count_all_rolls(dice)
selection = 12
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==0:
    print(test,'passed')
else:
    print(test,'failed')


#  setup for test 4 x expect pass
test = 'yah test good'
dice = [[1, True], [1, False], [1, True], [1, True], [1, False]]
dfrolls = count_all_rolls(dice)
selection = 12
dfscore = pd.read_csv('score_templatev2.csv')
dfscore = dfscore.set_index('result', drop=False)
if valid_selection(dfscore, selection, dice, dfrolls)==50:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'yahztee bonus->'
dice = [[3, True], [3, False], [4, True], [5, True], [3, False]]
dfrolls = count_all_rolls(dice)
# selection = 3
score = 9
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==0:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'yahztee no bonus but yahtzee->'
dice = [[3, True], [3, False], [3, True], [3, True], [3, False]]
dfrolls = count_all_rolls(dice)
# selection = 12
score = 50
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==0:
    print(test,'passed')
else:
    print(test,'failed')


#setup for test - expect failure
test = 'yahztee bonus obtained'
dice = [[3, True], [3, False], [3, True], [3, True], [3, False]]
dfrolls = count_all_rolls(dice)
# selection = 12
score = 15
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==100:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'yahztee bonus double not obtained'
dice = [[3, True], [3, False], [3, True], [3, True], [2, False]]
dfrolls = count_all_rolls(dice)
# selection = 12
score = 15
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfbonus['yah_bonus']=100
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==100:
    print(test,'passed')
else:
    print(test,'failed')


#setup for test - expect failure
test = 'final scoring'
# dice = [[3, True], [3, False], [3, True], [3, True], [2, False]]
# dfrolls = count_all_rolls(dice)
# selection = 12
# score = 15
dfscore = pd.read_csv('score_test.csv')
dfbonus = pd.read_csv('bonus_test.csv')
dfbonus['yah_bonus']=100
dfscore = dfscore.set_index('result', drop=False)
choice = compute_score(dfscore, dfbonus)
print(choice)

