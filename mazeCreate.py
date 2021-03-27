import PySimpleGUI as sg
import numpy as np
import math
import random


AppFont = 'Any 16'
sg.theme('DarkGrey5')
_VARS = {'cellCount': 10, 'gridSize': 400, 'canvas': False, 'window': False,
         'playerPos': [0, 0], 'cellMAP': False}
cellSize = _VARS['gridSize']/_VARS['cellCount']
exitPos = [_VARS['cellCount']-1, _VARS['cellCount']-1]



def makeMaze(dimX, dimY):
    """makes a maze by adding walls and holes in walls.

    Adds random vertical and horizontal lines and then cuts holes randomly.
    Mostly works, but not perfect.

    """

    # Make a starter gir of zeros:
    starterMap = np.zeros((dimX, dimY), dtype=int)
    # add rows and columns:
    for x in range(2):
        randRow = random.randint(1, dimX)
        randColumn = random.randint(1, dimY)
        starterMap[randRow-1:randRow] = 1
        starterMap[:, randColumn-1] = 1
        # poke holes in said rows and columns:
        for x in range(4):
            starterMap[randRow-1][random.randint(0, dimY-1)] = 0
            starterMap[random.randint(0, dimX-1)][randColumn-1] = 0
    # Add blank cells fro entrance,exit and around them:
    starterMap[0][0] = 0
    starterMap[0][1] = 0
    starterMap[1][0] = 0
    starterMap[dimX-1][dimY-1] = 0
    starterMap[dimX-1][dimY-2] = 0
    starterMap[dimX-2][dimY-1] = 0
    starterMap[dimX-2][dimY-2] = 0
    # print (starterMap)
    return starterMap


_VARS['cellMAP'] = makeMaze(_VARS['cellCount'], _VARS['cellCount'])


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
    for row in range(_VARS['cellMAP'].shape[0]):
        for column in range(_VARS['cellMAP'].shape[1]):
            if(_VARS['cellMAP'][column][row] == 1):
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
           sg.Text('', key='-exit-', font=AppFont, size=(15, 1)),
           sg.Button('NewMaze', font=AppFont)]]

_VARS['window'] = sg.Window('Random Puzzle Generator', layout, resizable=True, finalize=True,
                            return_keyboard_events=True)
_VARS['canvas'] = _VARS['window']['canvas']
drawGrid()
drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1], 'TOMATO')
drawCell(exitPos[0]*cellSize, exitPos[1]*cellSize, 'Black')
placeCells()


while True:             # Event Loop
    event, values = _VARS['window'].read()
    if event in (None, 'Exit'):
        break

    if event == 'NewMaze':
        _VARS['playerPos'] = [0, 0]
        _VARS['cellMAP'] = makeMaze(_VARS['cellCount'], _VARS['cellCount'])
    
    # Filter key press
    xPos = int(math.ceil(_VARS['playerPos'][0]/cellSize))
    yPos = int(math.ceil(_VARS['playerPos'][1]/cellSize))    

    if checkEvents(event) == 'Up':
        if int(_VARS['playerPos'][1] - cellSize) >= 0:
            if _VARS['cellMAP'][yPos-1][xPos] != 1:
                _VARS['playerPos'][1] = _VARS['playerPos'][1] - cellSize
    elif checkEvents(event) == 'Down':
        if int(_VARS['playerPos'][1] + cellSize) < _VARS['gridSize']-1:
            if _VARS['cellMAP'][yPos+1][xPos] != 1:
                _VARS['playerPos'][1] = _VARS['playerPos'][1] + cellSize
    elif checkEvents(event) == 'Left':
        if int(_VARS['playerPos'][0] - cellSize) >= 0:
            if _VARS['cellMAP'][yPos][xPos-1] != 1:
                _VARS['playerPos'][0] = _VARS['playerPos'][0] - cellSize
    elif checkEvents(event) == 'Right':
        if int(_VARS['playerPos'][0] + cellSize) < _VARS['gridSize']-1:
            if _VARS['cellMAP'][yPos][xPos+1] != 1:
                _VARS['playerPos'][0] = _VARS['playerPos'][0] + cellSize

    # Clear canvas, draw grid and cells
    _VARS['canvas'].TKCanvas.delete("all")
    drawGrid()
    drawCell(exitPos[0]*cellSize, exitPos[1]*cellSize, 'Black')
    drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1], 'TOMATO')
    placeCells()

    # Check for Exit:
    xPos = int(math.ceil(_VARS['playerPos'][0]/cellSize))
    yPos = int(math.ceil(_VARS['playerPos'][1]/cellSize))
    if [xPos, yPos] == exitPos:
        _VARS['window']['-exit-'].update('Found the exit !')
    else:
        _VARS['window']['-exit-'].update('')

_VARS['window'].close()
