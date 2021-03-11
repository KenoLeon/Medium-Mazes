import PySimpleGUI as sg
import numpy as np

AppFont = 'Any 16'
sg.theme('DarkGrey5')
_VARS = {'cellCount': 10, 'gridSize': 400, 'canvas': False, 'window': False}
cellMAP = np.random.randint(2, size=(_VARS['cellCount'], _VARS['cellCount']))
cellSize = _VARS['gridSize']/_VARS['cellCount']

# [[1 0 1 0 1 0 1 1]
#  [0 1 0 0 0 0 0 1]
#  [1 0 0 0 0 1 0 0]
#  [0 1 1 0 1 1 0 1]
#  [0 0 1 1 0 0 0 0]
#  [0 0 1 0 1 1 1 1]
#  [1 1 0 1 0 0 1 0]
#  [1 1 0 1 0 0 1 0]]

print(cellMAP)
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


def drawCell(x, y):
    _VARS['canvas'].TKCanvas.create_rectangle(
        x, y, x + cellSize, y + cellSize,
        outline='BLACK', fill='GREY', width=1)


def placeCells():
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            if(cellMAP[column][row] == 1):
                drawCell((cellSize*row), (cellSize*column))


# INIT :
layout = [[sg.Canvas(size=(_VARS['gridSize'], _VARS['gridSize']),
                     background_color='white',
                     key='canvas')],
          [sg.Exit(font=AppFont)]]

_VARS['window'] = sg.Window('GridMaker',
                            layout, resizable=True, finalize=True, return_keyboard_events=True)
_VARS['canvas'] = _VARS['window']['canvas']
drawGrid()
drawCell(40, 40)
# placeCells()


while True:             # Event Loop
    event, values = _VARS['window'].read()
    if event in (None, 'Exit'):
        break
    if callable(event):
        event()
_VARS['window'].close()





# window = sg.Window("Realtime Keyboard Test", layout, return_keyboard_events=True,
#                    use_default_focus=False)

# while True:
#     event, values = window.read(timeout=0)

#     if event == "OK":
#         print(event, values, "exiting")
#         break
#     if event is not sg.TIMEOUT_KEY:
#         if len(event) == 1:
#             if ord(event) == 63232:
#                 print('UP')
#             elif ord(event) == 63233:
#                 print('DOWN')
#             elif ord(event) == 63234:
#                 print('LEFT')
#             elif ord(event) == 63235:
#                 print('RIGHT')        
#             # print('%s - %s' % (event, ord(event)))
#         else:
#             print(event)
#     elif event == sg.WIN_CLOSED:
#         break

# window.close()