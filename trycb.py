# trycb.py

import PySimpleGUI as sg, sys

form = sg.FlexForm("Dynamic Combo")
col = [[sg.Checkbox("something1",key=1)], [sg.Checkbox("something2",key=2)],
    [sg.Checkbox("something3",key=3)], [sg.Checkbox("something4",key=4)],
    [sg.Checkbox("something5",key=5)], [sg.Checkbox("something6",key=6)],
    [sg.Checkbox("something7",key=7)], [sg.Checkbox("something8",key=8)],
    [sg.Checkbox("something9",key=9)], [sg.Checkbox("something10",key=10)],
    [sg.Checkbox("something11",key=11)], [sg.Checkbox("something12",key=12)],
    [sg.Checkbox("something13",key=13)], [sg.Checkbox("something14",key=14)],
    [sg.Checkbox("something15",key=15)], [sg.Checkbox("something16",key=16)],
    [sg.Checkbox("something17",key=17)], [sg.Checkbox("something18",key=18)]]
layout = [[sg.Text('<-- Scroll with Checkbox -->')],
    [sg.Button("SELECT ALL")], [sg.Button("DESELECT ALL")], 
    [sg.Column(col, size=(300,300), scrollable=True)],
    [sg.Cancel('Exit')]
]

form = sg.Window('Checkbox practice').Layout(layout)

while True:
    event, values = form.Read()
    if event == "SELECT ALL":  
        # IN THE RANGE ALWAYS PUT A NUMBER MORE TO GET THAT NUMBER
        for x in range(1,19):
            form.FindElement(x).Update(True)
    if event == "DESELECT ALL":  
         # IN THE RANGE ALWAYS PUT A NUMBER MORE TO GET THAT NUMBER
        for x in range(1,19):
            form.FindElement(x).Update(False)
    if event == "Exit":
        sys.exit()
