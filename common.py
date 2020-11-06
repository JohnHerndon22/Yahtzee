#common.py

import random
import ast
import os
import pandas as pd
import random
import os
import PySimpleGUI as sg

# def roll_die():
#     return random.randint(1,6)

def roll_selected_die(dice):
    # take the current dice set - reroll all of the dice that are NOT marked for hold (hold='*')
    # returns a table dicestr with the current rolls - to format the window
    currentTurn = list()
    for (roll,hold) in dice:
        if hold=='*':    
            pass
        else:
            roll = random.randint(1,6)
        currentTurn.append([roll, hold])
    
    dicestr = [['Value',str(currentTurn[0][0]),str(currentTurn[1][0]),str(currentTurn[2][0]),str(currentTurn[3][0]),str(currentTurn[4][0])],['Hold',currentTurn[0][1],currentTurn[1][1],currentTurn[2][1],currentTurn[3][1],currentTurn[4][1]]]
    # display_roll(currentTurn)
    return currentTurn, dicestr

def hold_some_die(currentTurn, holder_ch):
    # for the dice that are marked for hold - place a * in the value - comes from the game screen selections
    holders = []
    counter = 0
    holder_ch = holder_ch.strip()

    # format comes in as (#,#,#...) but needs rewritten for checkboxes
    for char_counter in range(len(holder_ch)):
        if holder_ch[char_counter]!=',':
            holders.append(int(holder_ch[char_counter]))
            counter=+1
    
    # clear current turn out
    for counter in range(5):
        currentTurn[counter][1]=' '
    
    for holdItem in holders:
        currentTurn[holdItem-1][1]='*'

    return currentTurn

def count_all_rolls(dice):
    # determine the number of each die rolled - used for scoring algorithm
    dfoutcomes = pd.DataFrame({'die': [1,2,3,4,5,6],
                                'rolls': [0,0,0,0,0,0]})                    
    # outcomes = [0,0,0,0,0,0]
    for (roll, hold) in dice:
        for index in range(6):
            if roll == index+1:
                dfoutcomes.loc[index, 'rolls']+=1
    return dfoutcomes

# def make_lower_selection(dfrolls, selection):
#     points = selection*dfrolls.loc[selection,'rolls']
#     # print(points, selection, dfrolls.loc[selection,'rolls'])
#     return points

def valid_selection(dfscore, selection, dfrolls, currentTurn):
    # validate the selection - return false if not valid - 0 points will be used
    if selection < 7:           # one of the under dice throws
        return True
    elif selection == 7:        # three of a kind
        if dfrolls['rolls'].max() > 2:
            return True
        else:
            return False
    elif selection == 8:        # four of a kind
        if dfrolls['rolls'].max() > 3:
            return True
        else:
            return False
    elif selection == 9:        # full house
        if dfrolls['rolls'].max() == 3 and dfrolls['rolls'].min() == 2:
            return True
        else:
            return False
    elif selection == 10:       # small straight
        ct_element = list()
        for ct in currentTurn:
            ct_element.append(ct[0])
        dfcurrentTurn = pd.DataFrame(ct_element,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 4:
            return False
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() == 3:
                return True
            else:
                return False      
        
    elif selection == 11:       # large straight
        ct_element = list()
        for ct in currentTurn:
            ct_element.append(ct[0])
        dfcurrentTurn = pd.DataFrame(ct_element,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 5:
            return False
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() == 4:
                return True
            else:
                return False    
    elif selection == 12:                   # yahtzee
        if dfrolls['rolls'].max() == 5:
            return True
        else:
            return False
    else:                                   # chance
        return True
    return True

# def askquestion(question):
#     selection_choices = ' '
#     update_window('selection_question',question,window)
#     update_window('selection_choices','  ',window)
#     event, values = window.read()
#     selection = int(values['selection_choices'])

#     return

def determine_score(dfrolls, dfscore, currentTurn, window):
    # the user has decided on the score - figure out if already used
    # validate when zero points will be used
    # return the points earned
    
    checking = True
    used = False
    while checking:
        if dfscore.loc[selection,'used']:
            update_window('selection_question','selection already made, try again: ',window)
            update_window('selection_choices','  ',window)
            event, values = window.read()
            selection = int(values['selection_choices'])
            checking = True
        else:
            if valid_selection(dfscore, selection, dfrolls, currentTurn):
                checking = False
            else:
                update_window('selection_question','selection will return zero points...are you sure (y/n)? ',window)
                update_window('selection_choices','  ',window)
                event, values = window.read()
                selection = values['selection_choices']
            
                # selection = input("selection will return zero points...are you sure (y/n)? ")
                if selection == 'y':
                    checking = False
                    used = True
                else:
                    update_window('selection_question','invalid selection...try again: ',window)
                    update_window('selection_choices','  ',window)
                    event, values = window.read()
                    selection = values['selection_choices']
                    checking = True
    value = 1 
    if used == True:
        points = 0
        value = 0
    else:
        if selection < 7:
            points = selection*dfrolls.loc[selection,'rolls']
            value = dfrolls.loc[selection,'rolls']
        elif selection in [7,8,13]:
            dfrolls['mult'] = dfrolls['rolls']*dfrolls['die']
            points = dfrolls['mult'].sum()
        elif selection == 9: 
            points = 25
        elif selection == 10: 
            points = 30
        elif selection == 11: 
            points = 40
        else: 
            points = 50
    
    return points, selection, value


def process_result(dfscore, currentTurn, dfrolls, window):
    # master function to determine the score earned - calls the determine_score and validate_score functions above
    dfrolls = count_all_rolls(currentTurn)
    dfrolls = dfrolls.set_index('die', drop=False)
    points, maxValue, maxRolls = determine_score(dfrolls, dfscore, currentTurn, window)
    
    dfscore.loc[maxValue,'maxRolls'] = maxRolls
    dfscore.loc[maxValue,'score'] = points
    dfscore.loc[maxValue, 'used'] = True

    return dfscore

def initialize_score_table(dfscore):
    # loads the scoring table - called from initialze window and if score if updated
    # dont load selectors with the bonuses
    fontdef = 'Helvetica 18'
    dfscoredisplay=dfscore[['result','comment','score']]
    sblayout = [[sg.Text('Selection      Result       Points',font=fontdef)]]
    for index, score in dfscoredisplay.iterrows():
        sblayout.append([sg.Text(str(score.result),font=fontdef),sg.Text(str(score.comment),font=fontdef),sg.Text(str(score.score),font=fontdef),sg.Checkbox('')])

    print(sblayout)
    return sblayout
    # dfscorelist = dfscoredisplay.values.tolist()

# comes out with the score table with the checkboxes - comnine this together
    # [sg.Text('Score:', font=fontdef)], 
    # [sg.Table(values=dfscorelist,headings=['Selection','Result','Points'],
    #     max_col_width=25, auto_size_columns=False, col_widths=11450, justification='center',num_rows=13,
    #     key='-SCORETABLE-', row_height=20,font=fontdef)],
    # [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
    #           [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
    #           [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],

    # return dfscorelist

def initialize_window_setup(dice, dfscore, num_roll, currentTurn):
    # loads the scoring table at the start
    sg.theme('BluePurple')   # Add a touch of color
    fontdef = 'Helvetica 18'
    
    sblayout = initialize_score_table(dfscore)
    # we will need a similar one fo the dice roll table
    
    # Initialize variable so that the window does not blow up - they are zero at this point
    total_score = 0 
    upper_bonus = 0
    extra_bonus = 0
    selection_choices = ''
    question = 'Hold #s?'
    
    dicestr = [['Value',str(currentTurn[0][0]),str(currentTurn[1][0]),str(currentTurn[2][0]),str(currentTurn[3][0]),str(currentTurn[4][0])],['Hold',currentTurn[0][1],currentTurn[1][1],currentTurn[2][1],currentTurn[3][1],currentTurn[4][1]]]
    
    # [sg.Table(values=dfscorelist,headings=['Selection','Result','Points'],
    #     max_col_width=25, auto_size_columns=False, col_widths=11450, justification='center',num_rows=13,
    #     key='-SCORETABLE-', row_height=20,font=fontdef)],
    
    # initialize the dice table
    layout = sblayout+[  
    [sg.Text('Score:', font=fontdef)], 
    [sg.Text('Upper Bonus: '+str(upper_bonus), font=fontdef)], 
    [sg.Text('Yahtzee Bonus: '+str(extra_bonus), font=fontdef)], 
    [sg.Text('Total Score: '+str(total_score), font=fontdef)], 
    [sg.Text(text='Roll: '+str(num_roll), font=fontdef, key='-NUMROLL-')],
    [sg.Table(values=dicestr,headings=['Die','1','2','3','4','5'],
        max_col_width=25, auto_size_columns=False, col_widths=11450, justification='center',num_rows=2,
        key='-ROLLTABLE-', row_height=20,font=fontdef)],
    [sg.Text(text=question, font=fontdef, key='selection_question'), sg.InputText(font=fontdef, key='selection_choices')],
    [sg.Button('Roll Again', font=fontdef), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)] 
    ]  

    # Create the Window
    window = sg.Window('Yaht-zee', layout).Finalize()
    # window = sg.Window('Yahtzee', layout).Finalize()      # throws an error
    
    return window

def update_window(element,value,window):
    # update elements of the window - probably not needed
    window[element].update(value)
    return

    # question = 'Which score to select?'
    # selection_choices = ''
    # update_window('selection_choices',question,window)
    

def compute_score():
    # compute the bonuses and set the score

    return
