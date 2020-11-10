# trybrokframe.py
import PySimpleGUI as sg
sg.theme('BluePurple')   # Add a touch of color
fontdef = 'Helvetica 18'

layout=[
    [sg.Frame('Score',[[sg.Text(str('ones'),font=fontdef, size=(10,1)),sg.Text(str(4),font=fontdef, size=(4,1)),sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=False, visible=True)]])]]
    
    
    # ,font=fontdef, size=(10,1)),sg.Text(str(4),font=fontdef, size=(4,1)),sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=False, visible=True)]]]
    
    
    # ,[sg.Text(str('twos'),font=fontdef, size=(10,1)),sg.Text(str(8),font=fontdef, size=(4,1)),sg.Radio('','-SCORE_SELECTOR-',font=fontdef, size=(1,1), disabled=False, visible=True)]]
# ]


window = sg.Window('Test Window', layout).Finalize()

event, values = window.read()

print(event)
print(values)