#yahtzee_roll_work.py

# import pandas as pd 
import random
import ast
import os
import pandas as pd
from common import *
import PySimpleGUI as sg

def initialize_dice():
    dice = [[0,False],[0,False],[0,False],[0,False],[0,False]]            
    return dice

def get_selection(values):
    
    for counter in range(12):
        if values[counter]:
            return counter+1
    return 0
    

def main():
    os.system("clear")
    # initialize overall variables
    dfscore = pd.read_csv('score_templatev2.csv')
    dfbonus = pd.read_csv('score_bonus.csv')
    dfscore = dfscore.set_index('result', drop=False)
      
    for turn in range(11):
        # 12 turns will fill the scoring 
        dice = initialize_dice()
        message_text = ''
            
        for num_roll in range(3):
            # each turn has three rolls - unless the user wants to score early
            dice = roll_selected_die(dice)
            # put this into a validation loop
            window, event, values = refresh_read_window(dice, dfscore, num_roll+1, dfbonus, message_text)
            window.close()
                    
            if event in (None, 'Quit'): # if user closes window or clicks cancel
                # ask do you really want to quit?
                return
            elif event in ('Select Score'):
                dfrolls = count_all_rolls(dice)
                radio_values = [values[index] for index in range(13)]
                
                if True in radio_values:
                    selection = get_selection(radio_values)
                    score = valid_selection(dfscore, selection, dice, dfrolls)
                    if score == 0:
                        # THIS HAS OK/CANCEL CAN I USE THOSE ITH Y/N IN STEAD?
                        if sg.popup_get_text('Score will provide zero points, are you sure (y/n)? ')!='y':
                            print('process zero score....')
                            # dfscore.loc[selection,'maxRolls'] = 0
                            dfscore.loc[selection,'score'] = score
                            dfscore.loc[selection, 'used'] = True
                            break
                        else:
                            message_text = 'select different score....'
                            continue
                    else:
                        # gGOING EARLY DID NOT FALL INTO THIS - CAN BACK WITH ZERO SCORE
                        print('process score now')
                        # dfscore.loc[selection,'maxRolls'] = maxRolls
                        dfscore.loc[selection,'score'] = score
                        dfscore.loc[selection, 'used'] = True
                        break
                else:
                    message_text = 'Select a score, dummy.....'
                    print('nothing selected....send back to window with message')    
                
            else:       # roll again was hit
                print(values)  # get the content of multiline via its unique ke
                print('this is roll again....')
                dice = hold_some_die(dice, values)

    print("Detailed score: ")
    print(dfscore)
    lower_bonus = 0

    if dfscore.loc[dfscore['result']<7,'score'].sum() > 62:
        lower_bonus = 35

    final_score = dfscore['score'].sum() +lower_bonus   
    print("final score is: ", final_score)


    return


main()

