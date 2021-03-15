#!/usr/bin/env python
# import sys
import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"
AppFont = 'Any 16'
layout = [[sg.Text("Press a key or scroll mouse")],
          [sg.Text("", size=(18, 1), key='text')],
          [sg.Exit(font=AppFont)]]

window = sg.Window("Keyboard Test", layout,
                   return_keyboard_events=True, use_default_focus=False)


while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    # Filter key press OSX :
    if len(event) == 1:
        if ord(event) == 63232: #UP
            print('UP')
        elif ord(event) == 63233: #DOWN
            print('DOWN')
        elif ord(event) == 63234: #LEFT
            print('LEFT')
        elif ord(event) == 63235: #RIGHT
            print('RIGHT')
    # Filter key press Windows :
    else:
        if event.startswith('Up'):
            print('UP')
        elif event.startswith('Down'):
            print('DOWN')
        elif event.startswith('Left'):
            print('LEFT')
        elif event.startswith('Right'):
            print('RIGHT')        

window.close()