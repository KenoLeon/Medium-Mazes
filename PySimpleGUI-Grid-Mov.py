import PySimpleGUI as sg
import numpy as np

AppFont = 'Any 16'
sg.theme('DarkGrey5')
_VARS = {'cellCount': 10, 'gridSize': 400, 'canvas': False, 'window': False,
         'playerPos': [0, 0]}
cellMAP = np.random.randint(2, size=(_VARS['cellCount'], _VARS['cellCount']))
cellSize = _VARS['gridSize']/_VARS['cellCount']

# METHODS:


def drawGrid():
    cells = _VARS['cellCount']
    _VARS['canvas'].TKCanvas.create_rectangle(
        1, 1, _VARS['gridSize'], _VARS['gridSize'],
        outline='BLACK', width=1)
    for x in range(cells):
        _VARS['canvas'].TKCanvas.create_line(
            ((cellSize * x), 0), ((cellSize * x), _VARS['gridSize']),
            fill='BLACK', width=1)
        _VARS['canvas'].TKCanvas.create_line(
            (0, (cellSize * x)), (_VARS['gridSize'], (cellSize * x)),
            fill='BLACK', width=1)


def drawCell(x, y):
    _VARS['canvas'].TKCanvas.create_rectangle(
        x, y, x + cellSize, y + cellSize,
        outline='BLACK', fill='GREY', width=1)


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
          [sg.Exit(font=AppFont)]]

_VARS['window'] = sg.Window('GridMaker',
                            layout, resizable=True, finalize=True,
                            return_keyboard_events=True)
_VARS['canvas'] = _VARS['window']['canvas']
drawGrid()
drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1])
# placeCells()


while True:             # Event Loop
    event, values = _VARS['window'].read()
    if event in (None, 'Exit'):
        break
    # Filter key press
    if checkEvents(event) == 'Up':
        _VARS['playerPos'][1] = _VARS['playerPos'][1] - 40
    elif checkEvents(event) == 'Down':
        _VARS['playerPos'][1] = _VARS['playerPos'][1] + 40
    elif checkEvents(event) == 'Left':
        _VARS['playerPos'][0] = _VARS['playerPos'][0] - 40
    elif checkEvents(event) == 'Right':
        _VARS['playerPos'][0] = _VARS['playerPos'][0] + 40
    # Clear canvas, draw grid and cells
    _VARS['canvas'].TKCanvas.delete("all")
    drawGrid()
    drawCell(_VARS['playerPos'][0], _VARS['playerPos'][1])

_VARS['window'].close()
