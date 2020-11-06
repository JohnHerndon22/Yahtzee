#yahtzee_roll_work.py

# import pandas as pd 
import random
import ast
import os
import pandas as pd
from common import *
import PySimpleGUI as sg



def main():
    os.system("clear")
    dfscore = pd.read_csv('score_templatev2.csv')
    dfbonus = pd.read_csv('score_bonus.csv')
    dfscore = dfscore.set_index('result', drop=False)
    counter = 1

    dice = [[0,' '],[0,' '],[0,' '],[0,' '],[0,' ']]            # eliminate this?  current turn is dice?
    dfrolls = pd.DataFrame()
    currentTurn = list()
    currentTurn, dicestr = roll_selected_die(dice)
    window = initialize_window_setup(dice, dfscore, 1, currentTurn)

    for turn in range(11):
     
        for num_roll in range(2):
            update_window('-ROLLTABLE-',dicestr,window)
            update_window('-NUMROLL-','Roll: '+str(num_roll+1),window)
            event, values = window.read()
            
            if event in (None, 'Quit'): # if user closes window or clicks cancel
                window.close()
                return
            else:
                print('You entered in the textbox:')
                print(values['selection_choices'])  # get the content of multiline via its unique ke
                currentTurn = hold_some_die(currentTurn, values['selection_choices'])
                currentTurn, dicestr = roll_selected_die(currentTurn)
                # update_window('-ROLLTABLE-',dicestr,window)
        
        update_window('-NUMROLL-','Roll: '+str(3),window)        
        dfscore = process_result(dfscore, currentTurn, dfrolls,window) 
        dfscorelist = initialize_score_table(dfscore)
        dice = [[0,' '],[0,' '],[0,' '],[0,' '],[0,' ']]
        dfrolls = pd.DataFrame()
        currentTurn = list()
        currentTurn, dicestr = roll_selected_die(dice)
        update_window('-SCORETABLE-',dfscorelist,window)
        update_window('-ROLLTABLE-',dicestr,window)
        update_window('selection_choices','  ',window)
        update_window('selection_question','Hold #s?',window)

    
        

    print("Detailed score: ")
    print(dfscore)
    lower_bonus = 0

    if dfscore.loc[dfscore['result']<7,'score'].sum() > 62:
        lower_bonus = 35

    final_score = dfscore['score'].sum() +lower_bonus   
    print("final score is: ", final_score)


    return


main()

