import numpy as np
import random

dimX = dimY = 6

def makeMaze(dimX, dimY):
    starterMap = np.zeros((dimX, dimY), dtype=int)
    randRow = random.randint(1, dimX)
    randColumn = random.randint(1, dimY)
    starterMap[randRow-1:randRow] = 1
    starterMap[randRow-1][random.randint(0, dimY-1)] = 0
    starterMap[:, randColumn-1] = 1
    starterMap[random.randint(0, dimX-1)][randColumn-1] = 0
    return starterMap


print(makeMaze(6,6))










# starterMap = np.zeros((dimX, dimY), dtype=int)
# randRow = random.randint(1, dimX)
# starterMap[randRow-1:randRow] = 1
# starterMap[randRow-1][random.randint(0, dimY-1)] = 0

# randColumn = random.randint(1, dimY)
# starterMap[:, randColumn-1] = 1

# print(repr(starterMap))

# array([[0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]])