# try dice window
import pandas as pd
import PySimpleGUI as sg
import random

sg.theme('BluePurple')   # Add a touch of color
fontdef = 'Helvetica 18'
dfscore = pd.read_csv('score_templatev2.csv')

# for testing
fontdef = 'Helvetica 18'
dfscoredisplay=dfscore[['result','comment','score','used']]
sbheader = [[sg.Text('Result          Points               Used',font=fontdef)]]

sblayout = [[sg.Text(str(score.comment),font=fontdef, size=(10,1)),
    sg.Text(str(score.score),font=fontdef, size=(9,1)),
    sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=score.used, visible=(not score.used))] for index, score in dfscoredisplay.iterrows()]

sblayout = sbheader+sblayout

sblayout += [[sg.Button('Roll Again', font=fontdef), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)]]
print(sblayout)

window = sg.Window('Test Window', sblayout).Finalize()

event, values = window.read()

print(event)
print(values)
print(sblayout)