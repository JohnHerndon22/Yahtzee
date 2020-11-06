# trycbtable.py

import PySimpleGUI as sg

layout = [[sg.Text('Checkboxes by table?')],
    [sg.Text('Dominio: '),
    sg.Checkbox('something', key='something1',default=True, disabled=True)], 
    [sg.Text('2nd Item: '),
    sg.Checkbox('something again', key='something2',default=False)],
    [sg.Button('Process')] 
    ]

window = sg.Window('Boxes', layout).Finalize()

event, values = window.read()

print(event)
print(values)