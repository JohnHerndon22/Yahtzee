# trypopupwin.py

import PySimpleGUI as sg
# set global options for window
background = 'Purple1'
sg.SetOptions(background_color=background,
    element_background_color=background,
    text_element_background_color=background,
    window_location=(750, 450),
    margins=(10,10),
    text_color = 'White',
    input_text_color ='Black',
    button_color = ('Black', 'gainsboro'))

layout = [[sg.Text('Zero Points will be Recorded - Proceed?')],[sg.Button('Yes'), sg.Button('No')]]

window = sg.Window('Test Window', layout, grab_anywhere=False, size=(280, 80), return_keyboard_events=True, finalize=True)

# window.Maximize()
window.BringToFront()
while True:
    event, values = window.read()
    if event in (None, 'No'):
        break
    else:
        sg.Popup('YES clicked', keep_on_top=True)
