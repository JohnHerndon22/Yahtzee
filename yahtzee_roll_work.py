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
    dfscore = dfscore.set_index('result', drop=False)
    # print(dfscore)
    
    for turn in range(11):

        stillRolling = True
        dice = [[0,False],[0,False],[0,False],[0,False],[0,False]]
        dfrolls = pd.DataFrame()
        currentTurn = list()
        currentTurn = roll_selected_die(dice)    

        for turn in range(2):
            currentTurn, stillRolling = hold_some_die(currentTurn)
            if stillRolling: 
                currentTurn = roll_selected_die(currentTurn)
            else:
                break

        dfscore = process_result(dfscore, currentTurn, dfrolls) 

    print("Detailed score: ")
    print(dfscore)
    lower_bonus = 0
    # df.loc[df['X'] == 1, 'Y'].sum()
    if dfscore.loc[dfscore['result']<7,'score'].sum() > 62:
        lower_bonus = 35

    final_score = dfscore['score'].sum() +lower_bonus   
    print("final score is: ", final_score)


    return


main()

