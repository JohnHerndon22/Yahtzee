# try dice window
import pandas as pd
import PySimpleGUI as sg
import random

sg.theme('BluePurple')   # Add a touch of color
fontdef = 'Helvetica 18'

# for testing
dice = [[random.randint(1,6),False],[random.randint(1,6),False],[random.randint(1,6),True],[random.randint(1,6),False],[random.randint(1,6),True]]   

dicelayout = [                
    [sg.Frame('Dice Roll',[[sg.Text('Roll:  ',font=fontdef, size=(4,1)),sg.Text(str(dice[0][0]),font=fontdef, size=(4,1)), sg.Text(str(dice[1][0]),font=fontdef, size=(4,1)), 
    sg.Text(str(dice[2][0]),font=fontdef, size=(4,1)), sg.Text(str(dice[3][0]),font=fontdef,size=(4,1)),
    sg.Text(str(dice[4][0]),font=fontdef)],
    [sg.Text('Hold: ',font=fontdef), sg.Checkbox('',font=fontdef,default=dice[0][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[1][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[2][1], size=(4,1)),sg.Checkbox('',font=fontdef,default=dice[3][1], size=(4,1)),
    sg.Checkbox('',font=fontdef,default=dice[4][1])]])],      
     [sg.Button('Roll Again', font=fontdef), sg.Button('Select Score', font=fontdef),sg.Button('Quit', font=fontdef)]
]

# for testing
window = sg.Window('Test Window', dicelayout).Finalize()

event, values = window.read()

print(event)
print(values)
# return sblayout