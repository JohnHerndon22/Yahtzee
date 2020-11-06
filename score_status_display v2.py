# batter_status_display.py


#!/usr/bin/env python
'''
Example of (almost) all widgets, that you can use in PySimpleGUI.
'''
import PySimpleGUI as sg
sg.change_look_and_feel('BluePurple')
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
numbers = [1,2,3,6,34,28939]

def create_window(running, counter):
    if running:
        layout = [
        [sg.Text('Processing Batter Status....', size=(
            30, 1), justification='left', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('espnid: ' + str(counter), key='output')]]
    
    else:
        layout = [
        [sg.Text('Processing Batter Status....', size=(
            30, 1), justification='left', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('espnid: ' + str(counter), key='output')],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

    return layout

counter = 1
layout = [[sg.Text('Processing Batter Status....', size=(30, 1), justification='left', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],[sg.Text('espnid: ' + str(counter), key='output')]]
window = sg.Window('MLB Batting', layout,default_element_size=(40, 1), grab_anywhere=False)

for counter in numbers:
    event, values = window.read(timeout=425)
    window['output'].update('espnid: {0}'.format(str(counter)))
    
layout = create_window(False, counter)
window = sg.Window('MLB Batting', layout,
        default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()    



sg.popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)