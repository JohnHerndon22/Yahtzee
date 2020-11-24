#yahtzee_roll_work.py

# import pandas as pd 
import random
import ast
import os
import pandas as pd
from common import *
import PySimpleGUI as sg


def main():
    
    while True:
        os.system("clear")
        # initialize overall variables
        dfscore = pd.read_csv('score_templatev2.csv')
        dfbonus = pd.read_csv('score_bonus.csv')
        dfgameresults = pd.read_csv('game_results.csv')
        # dfrolldecisions_all = pd.read_csv('roll_decisions.csv') 
        dfrolldecisions_game = pd.read_csv('roll_decisions_template.csv')
        gameid = dfgameresults['gameid'].max() + 1

        dfscore = dfscore.set_index('result', drop=False)
        pts_question = 'Zero Points will be Recorded - Proceed?'
        dice = initialize_dice()
        message_text = ''
        window = initialize_read_window(dice, dfscore, 1, dfbonus, message_text)

        for turn in range(13):
            # 12 turns will fill the scoring 
            num_roll = 1
            while True:  
            # for num_roll in range(3):
                # each turn has three rolls - unless the user wants to score early
                dice = roll_selected_die(dice)
                window, event, values, dfrolldecisions_game = refresh_read_window(dice, dfscore, num_roll, dfbonus, message_text, window, dfrolldecisions_game, gameid)
                message_text = ''

                if event in (None, 'Quit'): # if user closes window or clicks cancel
                    # ask do you really want to quit?
                    window.close()
                    return
                elif event in ('Select Score'):
                    # Hold all dice 
                    dfrolls = count_all_rolls(dice)                
                    radio_values = [values['used'+str(index+1)] for index in range(13)]
                    selection = get_selection(radio_values, dfscore)
                    if selection != 0:
                        score = valid_selection(dfscore, selection, dice, dfrolls)
                        if score == 0:
                            if ask_yesno_question(pts_question):
                                dfscore.loc[selection,'score'] = score
                                dfscore.loc[selection, 'used'] = True
                                dfrolldecisions_game['score'][dfrolldecisions_game.index.max()]=score
                                dice = initialize_dice()
                                break
                            else:
                                dice = hold_all_dice(dice)
                                message_text = 'select different score....'
                                continue
                        else:
                            
                            yah_bonus_eligible = (dfscore.loc[12,'score']==50) or (not dfscore.loc[12,'used'])            # get the previous score
                            dfscore.loc[selection,'score'] = score
                            dfscore.loc[selection, 'used'] = True
                            dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score, yah_bonus_eligible)
                            dfrolldecisions_game['score'][dfrolldecisions_game.index.max()]=score
                            dice = initialize_dice()
                            break
                    else:
                        dice = hold_all_dice(dice)
                        message_text = 'Select a score, dummy.....'
                        
                else:       # roll again was hit
                    num_roll+=1
                    dice = hold_some_die(dice, values)
                    print('after hold some die')
                    print(dice)
        
        window.close()
        if compute_score(dfscore, dfbonus, gameid, dfrolldecisions_game, True) == "Quit":
            return
        else:                   # if new game moves to the next
            continue


main()

