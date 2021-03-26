import PySimpleGUI as sg
import numpy as np
import math
AppFont = 'Any 16'
sg.theme('DarkGrey5')
_VARS = {'cellCount': 6, 'gridSize': 400, 'canvas': False, 'window': False,
         'playerPos': [0, 0], 'exit': [5, 5]}
cellSize = _VARS['gridSize']/_VARS['cellCount']

# Maze Map:
cellMAP = np.array([[0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]])

# METHODS:


def drawGrid():
    cells = _VARS['cellCount']
    _VARS['canvas'].TKCanvas.create_rectangle(
        1, 1, _VARS['gridSize'], _VARS['gridSize'], outline='BLACK', width=1)
    for x in range(cells):
        _VARS['canvas'].TKCanvas.create_line(
            ((cellSize * x), 0), ((cellSize * x), _VARS['gridSize']),
            fill='BLACK', width=1)
        _VARS['canvas'].TKCanvas.create_line(
            (0, (cellSize * x)), (_VARS['gridSize'], (cellSize * x)),
            fill='BLACK', width=1)


def drawCell(x, y, color='GREY'):
    _VARS['canvas'].TKCanvas.create_rectangle(
        x, y, x + cellSize, y + cellSize,
        outline='BLACK', fill=color, width=1)


def placeCells():
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            if(cellMAP[column][row] == 1):
                drawCell((cellSize*row), (cellSize*column))


def checkEvents(event):
    move = ''
    if len(event) == 1:
        if ord(event) == 63232:  # UP
            move = 'Up'
        elif ord(event) == 63233:  # DOWN
            move = 'Down'
        elif ord(event) == 63234:  # LEFT
            move = 'Left'
        elif ord(event) == 63235:  # RIGHT
            move = 'Right'
    # Filter key press Windows :
    else:
        if event.startswith('Up'):
            move = 'Up'
        elif event.startswith('Down'):
            move = 'Down'
        elif event.startswith('Left'):
            move = 'Left'
        elif event.startswith('Right'):
            move = 'Right'
    return move


# INIT :
layout = [[sg.Canvas(size=(_VARS['gridSize'], _VARS['gridSize']),
                     background_color='white',
                     key='canvas')],
          [sg.Exit(font=AppFont),
           sg.Text('', key='-exit-', font=AppFont, size=(15, 1))]]

_VARS['window'] = sg.Window('GridMaker', layout, resizable=True, finalize=True,
                            return_keyboard_events=True)
_VARS['canvas'] = _VARS['window']['canvas']
drawGrid()
drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1], 'TOMATO')
drawCell(_VARS['exit'][0]*cellSize, _VARS['exit'][1]*cellSize, 'Black')
placeCells()


while True:             # Event Loop
    event, values = _VARS['window'].read()
    if event in (None, 'Exit'):
        break

    # Filter key press, get users position
    xPos = int(math.ceil(_VARS['playerPos'][0]/cellSize))
    yPos = int(math.ceil(_VARS['playerPos'][1]/cellSize))    

    if checkEvents(event) == 'Up':
        if int(_VARS['playerPos'][1] - cellSize) >= 0:
            if cellMAP[yPos-1][xPos] != 1:
                _VARS['playerPos'][1] = _VARS['playerPos'][1] - cellSize
    elif checkEvents(event) == 'Down':
        if int(_VARS['playerPos'][1] + cellSize) < _VARS['gridSize']-1:
            if cellMAP[yPos+1][xPos] != 1:
                _VARS['playerPos'][1] = _VARS['playerPos'][1] + cellSize
    elif checkEvents(event) == 'Left':
        if int(_VARS['playerPos'][0] - cellSize) >= 0:
            if cellMAP[yPos][xPos-1] != 1:
                _VARS['playerPos'][0] = _VARS['playerPos'][0] - cellSize
    elif checkEvents(event) == 'Right':
        if int(_VARS['playerPos'][0] + cellSize) < _VARS['gridSize']-1:
            if cellMAP[yPos][xPos+1] != 1:
                _VARS['playerPos'][0] = _VARS['playerPos'][0] + cellSize

    # Clear canvas, draw grid and cells
    _VARS['canvas'].TKCanvas.delete("all")
    drawGrid()
    drawCell(_VARS['exit'][0]*cellSize, _VARS['exit'][1]*cellSize, 'Black')
    drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1], 'TOMATO')
    placeCells()

    # Check for Exit:
    xPos = int(math.ceil(_VARS['playerPos'][0]/cellSize))
    yPos = int(math.ceil(_VARS['playerPos'][1]/cellSize))
    if [xPos, yPos] == _VARS['exit']:
        _VARS['window']['-exit-'].update('Found the exit !')
    else:
        _VARS['window']['-exit-'].update('')    

_VARS['window'].close()
