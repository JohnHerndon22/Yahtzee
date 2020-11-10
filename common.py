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
    new_dice = list()
    for (roll,hold) in dice:
        if hold:    
            pass
        else:
            roll = random.randint(1,6)
        new_dice.append([roll, hold])
    
    return new_dice

def hold_some_die(dice, boxes_marked):
    # for the dice that are marked for hold - place a * in the value - comes from the game screen selections
    
    # format comes in as (#,#,#...) but needs rewritten for checkboxes
    for counter in range(5):
        dice[counter][1]=False
        if boxes_marked[counter+13]:
            dice[counter][1]=True

    return dice

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

def valid_selection(dfscore, selection, dice, dfrolls):
    # validate the selection - return false if not valid - 0 points will be used
    
    if selection < 7:           # one of the under dice throws
        return process_score(dfscore, selection, dice, dfrolls)
    elif selection == 7:        # three of a kind
        if dfrolls['rolls'].max() > 2:
            return process_score(dfscore, selection, dice, dfrolls)
        else:
            return 0
    elif selection == 8:        # four of a kind
        if dfrolls['rolls'].max() > 3:
            return process_score(dfscore, selection, dice, dfrolls)
        else:
            return 0
    elif selection == 9:        # full house
        if dfrolls['rolls'].max() == 3 and dfrolls['rolls'].min() == 2:
            return process_score(dfscore, selection, dice, dfrolls)
        else:
            return 0
    elif selection == 10:       # small straight
        ct_element = list()
        for ct in dice:
            ct_element.append(ct[0])
        dfcurrentTurn = pd.DataFrame(ct_element,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 4:
            return 0
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() == 3:
                return process_score(dfscore, selection, dice, dfrolls)
            else:
                return 0      
        
    elif selection == 11:       # large straight
        ct_element = list()
        for ct in currentTurn:
            ct_element.append(ct[0])
        dfcurrentTurn = pd.DataFrame(ct_element,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 5:
            return 0
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() == 4:
                return process_score(dfscore, selection, dice, dfrolls)
            else:
                return 0    
    elif selection == 12:                   # yahtzee
        if dfrolls['rolls'].max() == 5:
            return process_score(dfscore, selection, dice, dfrolls)
        else:
            return 0
    else:                                   # chance
        return process_score(dfscore, selection, dice, dfrolls)
    return process_score(dfscore, selection, dice, dfrolls)

def process_score(dfscore, selection, dice, dfrolls):
    # function to determine the score earned - calls the determine_score and validate_score functions above
    if selection < 7:
            points = selection*dfrolls.loc[selection,'rolls']
            # value = dfrolls.loc[selection,'rolls']
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

    # dfscore.loc[selection,'maxRolls'] = maxRolls
    # dfscore.loc[selection,'score'] = points
    # dfscore.loc[selection, 'used'] = True

    return points

def refresh_dice_table(dice):
    # refreshes the dice roll onto the screen - once the window is read - the user can select holds
    # called from init window and roll dice
    fontdef = 'Helvetica 18'
    dicelayout = []
    dicelayout = [[sg.Text('Roll:  ',font=fontdef, size=(4,1)),sg.Text(str(dice[0][0]),font=fontdef, size=(4,1)), sg.Text(str(dice[1][0]),font=fontdef, size=(4,1)), 
    sg.Text(str(dice[2][0]),font=fontdef, size=(4,1)), sg.Text(str(dice[3][0]),font=fontdef,size=(4,1)), sg.Text(str(dice[4][0]),font=fontdef)],
    [sg.Text('Hold: ',font=fontdef), sg.Checkbox('',font=fontdef,default=dice[0][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[1][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[2][1], size=(4,1)),sg.Checkbox('',font=fontdef,default=dice[3][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[4][1])]]
    
    # [[sg.Frame('Dice Roll',
    # , [sg.Button('Roll Again', font=fontdef), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)]
    # # print(sblayout)
    return dicelayout

def refresh_score_table(dfscore):
    # loads the scoring table - called from initialze window and if score if updated
    # dont load selectors with the bonuses
    # for testing
    fontdef = 'Helvetica 18'
    dfscoredisplay=dfscore[['result','comment','score','used']]
    sbheader = [[sg.Text('Result          Points               Used',font=fontdef)]]
    sblayout = [[sg.Text(str(score.comment),font=fontdef, size=(10,1)),
        sg.Text(str(score.score),font=fontdef, size=(9,1)),
        sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=score.used, visible=(not score.used))] for index, score in dfscoredisplay.iterrows()]

    sblayout = sbheader+sblayout

    return sblayout

def refresh_read_window(dice, dfscore, num_roll, dfbonus, message_text):
    # setup the window at the start of the game

    # roll again is disabled if num_roll = 3
    # make the question an input box - callable from anywhere - not on the screen
    # select score button is not available until a radio button is hit

    sg.theme('BluePurple')   # Add a touch of color
    fontdef = 'Helvetica 18'
    
    if num_roll==3: 
        disable_rollagain = True
    else: 
        disable_rollagain = False
        
    sblayout = refresh_score_table(dfscore)
    dicelayout = refresh_dice_table(dice)
    
    # Initialize variables - they are zero at the start of the game
    total_score = 0 
    upper_bonus = str(dfbonus['upper_bonus'][0])
    extra_bonus = str(dfbonus['yah_bonus'][0])
    
    layout = [[sg.Text('Score:', font=fontdef)], 
    sblayout[0],sblayout[1],sblayout[2],sblayout[3],sblayout[4],sblayout[5],
    sblayout[6],sblayout[7],sblayout[8],sblayout[9],sblayout[10],sblayout[11],sblayout[12],sblayout[13],
    [sg.Text('Upper Bonus: '+str(upper_bonus), font=fontdef)], 
    [sg.Text('Yahtzee Bonus: '+str(extra_bonus), font=fontdef)], 
    [sg.Text('Total Score: '+str(total_score), font=fontdef)],
    [sg.Text(text='Roll: '+str(num_roll), font=fontdef, key='-NUMROLL-')],
    dicelayout[0],dicelayout[1],  
    [sg.Text(text=message_text, font=fontdef, key='message')], 
    [sg.Button('Roll Again', font=fontdef, disabled=disable_rollagain), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)] 
    ]

    # Create the Window
    window = sg.Window('Yaht-zee', layout).Finalize()
    # window = sg.Window('Yahtzee', layout).Finalize()      # throws an error
    
    event, values = window.read()
    print(event, values)
    # did they push select score but no score was selected?
    
    return window, event, values

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
