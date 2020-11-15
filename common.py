#common.py

import random
import ast
import os
import pandas as pd
import random
import os
import PySimpleGUI as sg

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

    for counter in range(5):
        dice[counter][1]=False
        if boxes_marked['hold'+str(counter+1)]:
            dice[counter][1]=True

    return dice

def count_all_rolls(dice):
    # determine the number of each die rolled - used for scoring algorithm
    dfrolls = pd.DataFrame({'die': [1,2,3,4,5,6],
                                'rolls': [0,0,0,0,0,0]})                    

    for (roll, hold) in dice:
        for index in range(6):
            if roll == index+1:
                dfrolls.loc[index, 'rolls']+=1
    dfrolls = dfrolls.set_index('die')
    return dfrolls

def determine_bonus(dfbonus, dfscore, dfrolls, score):

    # determine if upper bonus reached
    if int(dfbonus['upper_bonus']) == 0:
        if dfscore.loc[dfscore.index<7,'score'].sum() > 62:
            dfbonus['upper_bonus'] = 35

    # determine yahtzee bonus
    if (score != 50) and (dfrolls['rolls'].max()==5):
            start_bonus = int(dfbonus['yah_bonus'])
            dfbonus['yah_bonus'] = start_bonus+100
            
    return dfbonus


def valid_selection(dfscore, selection, dice, dfrolls):
    # validate the selection - return false if not valid - 0 points will be used
    
    if selection < 7:           # one of the under dice throws
        return selection*dfrolls.loc[selection,'rolls']
    elif selection == 7:        # three of a kind
        if dfrolls['rolls'].max() > 2:
            return sum([item[0] for item in dice])
        else:
            return 0
    elif selection == 8:        # four of a kind
        if dfrolls['rolls'].max() > 3:
            return sum([item[0] for item in dice])
        else:
            return 0
    elif selection == 9:        # full house
        if dfrolls['rolls'].max() == 3 and dfrolls['rolls'].mask(dfrolls['rolls']==0).min().min()==2:
            return 25
        else:
            return 0
    elif selection == 10:       # small straight

        rolls = [item[0] for item in dice]
        dfcurrentTurn = pd.DataFrame(rolls,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 4:
            return 0
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() >= 3:
                return 30
            else:
                return 0      
        
    elif selection == 11:       # large straight
 
        rolls = [item[0] for item in dice]
        dfcurrentTurn = pd.DataFrame(rolls,columns=['roll'])
        dfcurrentTurn = pd.DataFrame.drop_duplicates(dfcurrentTurn)
        if len(dfcurrentTurn.index) < 5:
            return 0
        else:
            if dfcurrentTurn['roll'].max() - dfcurrentTurn['roll'].min() == 4:
                return 40
            else:
                return 0  

    elif selection == 12:                   # yahtzee
        if dfrolls['rolls'].max() == 5:
            return 50
        else:
            return 0
    else:                                   # chance
        return sum([item[0] for item in dice])
    return 0

def process_score(dfscore, selection, dice, dfrolls):
    # not needed
    
    # function to determine the score earned - calls the determine_score and validate_score functions above
    if selection < 7:
            points = selection*dfrolls.loc[selection,'rolls']
            # value = dfrolls.loc[selection,'rolls']
    elif selection in [7,8,13]:
        dfrolls['mult'] = dfrolls['rolls']*dfrolls['index']
        points = dfrolls['mult'].sum()
    elif selection == 9: 
        points = 25
    elif selection == 10: 
        points = 30
    elif selection == 11: 
        points = 40
    else: 
        points = 50

    return points

def refresh_dice_table(dice):
    # refreshes the dice roll onto the screen - once the window is read - the user can select holds
    # called from init window and roll dice
    fontdef = 'Helvetica 18'
    dicelayout = []
    dicelayout = [[sg.Text('Roll:  ',font=fontdef, size=(4,1)),sg.Text(str(dice[0][0]),font=fontdef, size=(4,1), key='dice1'), sg.Text(str(dice[1][0]),font=fontdef, size=(4,1), key='dice2'), 
    sg.Text(str(dice[2][0]),font=fontdef, size=(4,1), key='dice3'), sg.Text(str(dice[3][0]),font=fontdef,size=(4,1), key='dice4'), sg.Text(str(dice[4][0]),font=fontdef, key='dice5')],
    [sg.Text('Hold: ',font=fontdef), sg.Checkbox('',font=fontdef,default=dice[0][1], size=(4,1), key='hold1'),
    sg.Checkbox('',font=fontdef,default=dice[1][1], size=(4,1), key='hold2'),
    sg.Checkbox('',font=fontdef,default=dice[2][1], size=(4,1), key='hold3'),
    sg.Checkbox('',font=fontdef,default=dice[3][1], size=(4,1), key='hold4'),
    sg.Checkbox('',font=fontdef,default=dice[4][1], key='hold5')]]
 
    return dicelayout

def refresh_score_table(dfscore):
    # loads the scoring table - called from initialze window and if score if updated
    # dont load selectors with the bonuses
    # for testing
    fontdef = 'Helvetica 18'
    usedstr = 'used'
    dfscoredisplay=dfscore[['result','comment','score','used']]
    sbheader = [[sg.Text('Result          Points               Used',font=fontdef)]]
    sblayout = [[sg.Text(str(score.comment),font=fontdef, size=(10,1)),
        sg.Text(str(score.score),font=fontdef, size=(9,1),key='score'+str(index)),
        sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=score.used, visible=(not score.used),key=usedstr+str(index))] for index, score in dfscoredisplay.iterrows()]

    sblayout = sbheader+sblayout

    return sblayout

def initialize_read_window(dice, dfscore, num_roll, dfbonus, message_text):
    # setup and initialize the window at the start of the game

    sg.theme('BluePurple')   # Add a touch of color
    fontdef = 'Helvetica 18'
    
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
    [sg.Text('Upper Bonus: '+str(upper_bonus), font=fontdef, size=(15,1),key="upperbonus")], 
    [sg.Text('Yahtzee Bonus: '+str(extra_bonus), font=fontdef, size=(15,1), key="yahbonus")], 
    [sg.Text('Total Score: '+str(total_score), font=fontdef, size=(15,1), key="totalscore")],
    [sg.Text(text='Roll: '+str(num_roll), font=fontdef, key='-NUMROLL-')],
    dicelayout[0],dicelayout[1],  
    [sg.Text(text=message_text, font=fontdef, key='message', size=(20,1))], 
    [sg.Button('Roll Again', font=fontdef, disabled=disable_rollagain,key='rollagain'), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)] 
    ]

    # Create the Window
    window = sg.Window('Yaht-zee', layout).Finalize()
    # window = sg.Window('Yahtzee', layout).Finalize()      # throws an erroR

    # no read here - we will use the refersh window (below) to do the read
    
    return window

def refresh_read_window(dice, dfscore, num_roll, dfbonus, message_text, window):
    # refresh the window at the start of the game - get the score and ask for a button/radio/checkbox push

    # roll again is disabled if num_roll = 3
    if num_roll==3: 
        disable_rollagain = True
    else: 
        disable_rollagain = False
        
    sblayout = refresh_score_table(dfscore)
    dicelayout = refresh_dice_table(dice)
    
    upper_bonus = str(dfbonus['upper_bonus'][0])
    extra_bonus = str(dfbonus['yah_bonus'][0])
    total_score = dfscore['score'].sum() 
    total_score = int(total_score) + int(upper_bonus) + int(extra_bonus)
    
    update_window('-NUMROLL-','Roll: '+str(num_roll), window)
    update_window('upperbonus','Upper Bonus: '+str(upper_bonus), window)
    update_window('yahbonus','Yahtzee Bonus: '+str(extra_bonus), window)
    update_window('totalscore','Total Score: '+str(total_score), window)
    update_window('message', message_text, window) 
    window['rollagain'].update(disabled=disable_rollagain)
    
    for index, score in dfscore.iterrows():
        window['used'+str(index)].update(disabled=score.used, visible=(not score.used))
        window['score'+str(index)].update(str(score.score))
        
    for i in [index for index in range(5)]:
        update_window('dice' + str(i+1),str(dice[i][0]),window)
    
    for i in [index for index in range(5)]:
        update_window('hold' + str(i+1),dice[i][1],window)

    event, values = window.read()

    return window, event, values

def update_window(element,value,window):
    # update elements of the window 
    window[element].update(value=value)
    return

def initialize_dice():
    dice = [[0,False],[0,False],[0,False],[0,False],[0,False]]            
    return dice

def hold_all_dice(dice):
    dice[1][1] = True
    dice[2][1] = True
    dice[3][1] = True
    dice[4][1] = True
    dice[0][1] = True
    
    return dice

def get_selection(values, dfscore):
    
    for counter in range(13):
        #qqqq
        if values[counter]: 
            if dfscore.loc[counter+1,'score']==0:
                return counter+1
    return 0

def ask_yesno_question(question):
    sg.theme('BluePurple')   # Add a touch of color
    fontdef = 'Helvetica 18'
    sg.SetOptions(window_location=(750, 350),
        margins=(10,10),
        font=fontdef)

    layout = [[sg.Text('Zero Points will be Recorded - Proceed?')],[sg.Button('Yes'), sg.Button('No')]]

    window = sg.Window('Scoring', layout, grab_anywhere=False, size=(380,95), return_keyboard_events=True, finalize=True)

    # window.Maximize()
    window.BringToFront()
    event, values = window.read()
    window.close()
    if event in (None, 'No'):
        return False
    else:
        return True
    return 



def compute_score(dfscore, dfbonus):
    # called from main window to figure out if bonuses were earned

    sg.theme('BluePurple')   # Add a touch of color
    fontdef = 'Helvetica 18'

    dfscoredisplay=dfscore[['comment','score']]
    upper_bonus = str(dfbonus['upper_bonus'][0])
    extra_bonus = str(dfbonus['yah_bonus'][0])
    total_score = dfscore['score'].sum() 
    total_score = int(total_score) + int(upper_bonus) + int(extra_bonus)

    sblayout = [[sg.Text(str(score.comment),font=fontdef, size=(20,1)),
            sg.Text(str(score.score),font=fontdef, size=(9,1))] for index, score in dfscoredisplay.iterrows()]

    layout = [  [sg.Text('Final Score', font=fontdef)], 
                [sg.Text('Result                               Score', font=fontdef)], 
                sblayout[0],sblayout[1],sblayout[2],sblayout[3],sblayout[4],sblayout[5],
                sblayout[6],sblayout[7],sblayout[8],sblayout[9],sblayout[10],sblayout[11],sblayout[12],
                [sg.Text('-----------------------------', font=fontdef)],
                [sg.Text('Upper Bonus: ' +str(upper_bonus), font=fontdef)],
                [sg.Text('Yahtzee Bonus: ' +str(extra_bonus), font=fontdef)],
                [sg.Text('Total Score: ' +str(total_score), font=fontdef)],
                [sg.Text('', font=fontdef)],
                [sg.Button('New Game', font=fontdef), sg.Button('Quit',font=fontdef)]  ]

    window = sg.Window('Yahtzee Game Results', layout, size=(400,660)).Finalize()

    event, values = window.read()
    window.close()

    if event in (sg.WIN_CLOSED, 'Quit'):
        return 'Quit'
    if event == 'New Game':
        return 'New Game'

        
    