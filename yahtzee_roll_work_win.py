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
                window, event, values = refresh_read_window(dice, dfscore, num_roll, dfbonus, message_text, window)
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
                                dice = initialize_dice()
                                break
                            else:
                                dice = hold_all_dice(dice)
                                message_text = 'select different score....'
                                continue
                        else:
                            
                            dfscore.loc[selection,'score'] = score
                            dfscore.loc[selection, 'used'] = True
                            dfbonus = determine_bonus(dfbonus, dfscore, dfrolls, score)
                            dice = initialize_dice()
                            break
                    else:
                        dice = hold_all_dice(dice)
                        message_text = 'Select a score, dummy.....'
                        
                else:       # roll again was hit
                    num_roll+=1
                    dice = hold_some_die(dice, values)
        
        window.close()
        if compute_score(dfscore, dfbonus) == "Quit":
            return
        else:                   # if new game moves to the next
            continue


main()

