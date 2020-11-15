# trymline1.py

import PySimpleGUI as sg
import pandas as pd
from tabulate import tabulate

dfscore = pd.read_csv('score_templatev2.csv')
dfbonus = pd.read_csv('score_bonus.csv')
dfscoredisplay=dfscore[['comment','score']]

sg.theme('BluePurple')   # Add a touch of color
fontdef = 'Helvetica 18'

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

while True:             # Event Loop
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Quit'):
        break
    if event == 'New Game':
        window['-OUTPUT-'].update('New Game....')

window.close()