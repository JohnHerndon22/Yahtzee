#test_yahtzee.py

import pandas as pd
from common import *


# test = 'store game decision - final'
# print(test)
# dfrolldecisions_game = pd.read_csv('declog.csv')
# # dice = [[3, True], [3, True], [4, True], [5, True], [3, False]]
# # values = {'hold1': False, 'hold2': True, 'hold3': True, 'hold4': False, 'hold5': True}
# gameid = 'test_1000'
# dfscore = pd.read_csv('score_templatev2.csv')
# dfbonus = pd.read_csv('score_bonus_test.csv')
# dfbonus['yah_bonus']=100
# # dfscore = dfscore.set_index('result', drop=False)
# # choice = compute_score(dfscore, dfbonus, gameid)
# print('the choice is: ' + compute_score(dfscore, dfbonus, gameid, dfrolldecisions_game, False))
# dfrolldecisions_all = pd.read_csv('roll_decisions_test.csv')
# print('df all roll decisions: ')
# print(dfrolldecisions_all)

test = 'ROLLS DICE - SAME?'
dice = [[1, False], [2, True], [5, True], [6, True], [3, True]]
before_dice = dice
dif_role = 0

for x in range(100):
    dice = roll_selected_die(dice)
    if dice[0][0]==before_dice[0][0]:
        print('matches')
    else:
        print('different role')
        dif_role +=1
    dice = before_dice

print('results are: ',str(dif_role),' out of 100')
quit()

# roll selected die - after
# [[6, False], [2, True], [5, True], [6, True], [3, True]]
# roll selected die - before
# [[0, False], [0, False], [0, False], [0, False], [0, False]]
# roll selected die - after
# [[4, False], [3, False], [6, False], [1, False], [1, False]]
# after hold some die
# [[4, True], [3, True], [6, True], [1, False], [1, False]]
# roll selected die - before
# [[4, True], [3, True], [6, True], [1, False], [1, False]]
# roll selected die - after
# [[4, True], [3, True], [6, True], [1, False], [1, False]]
# after hold some die
# [[4, True], [3, True], [6, True], [1, False], [1, False]]
# roll selected die - before
# [[4, True], [3, True], [6, True], [1, False], [1, False]]
# roll selected die - after
# [[4, True], [3, True], [6, True], [3, False], [2, False]]

test = 'store game decision - working?'
print(test)
dice = [[3, True], [3, True], [4, True], [5, True], [3, False]]
values = {'hold1': False, 'hold2': True, 'hold3': True, 'hold4': False, 'hold5': True}
gameid = 'test_1000'
print(store_game_decision(values, dice, gameid))



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
test = 'yahztee bonus-> bug still here?'
dice = [[3, True], [3, False], [3, True], [3, True], [3, False]]
dfrolls = count_all_rolls(dice)
# selection = 3
score = 9
dfscore = pd.read_csv('score_yah_test.csv')             # has yahtzee = True
dfbonus = pd.read_csv('score_bonus.csv')                # blank bonus = 0
dfscore = dfscore.set_index('result', drop=False)
yah_bonus_eligible = (dfscore.loc[12,'score']==50) and (dfscore.loc[12,'used'])
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
# determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
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
yah_bonus_eligible = True
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
# should not return bonus = score = 50
if int(dfbonus['yah_bonus'])==0:
    print(test,'passed')
else:
    print(test,'failed')


#setup for test - expect failure
test = 'yahztee bonus obtained'
dice = [[3, True], [3, False], [2, True], [3, True], [3, False]]
dfrolls = count_all_rolls(dice)
# selection = 12
score = 15
yah_bonus_eligible = True
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==0:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
test = 'yahztee bonus double not obtained'
dice = [[3, True], [3, False], [3, True], [3, True], [3, False]]
dfrolls = count_all_rolls(dice)
yah_bonus_eligible = True
score = 15
dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfbonus['yah_bonus']=100
dfscore = dfscore.set_index('result', drop=False)
dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
print('yahtzee bonus: ' + str(int(dfbonus['yah_bonus'])))
if int(dfbonus['yah_bonus'])==200:
    print(test,'passed')
else:
    print(test,'failed')

#setup for test - expect failure
# test = 'final scoring'
# # dice = [[3, True], [3, False], [3, True], [3, True], [2, False]]
# # dfrolls = count_all_rolls(dice)
# # selection = 12
# gameid = 20
# dfscore = pd.read_csv('score_test_yah.csv')
# dfbonus = pd.read_csv('bonus_test.csv')
# dfbonus['yah_bonus']=100
# dfscore = dfscore.set_index('result', drop=False)
# choice = compute_score(dfscore, dfbonus, gameid)
# print(choice)

