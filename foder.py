import numpy as np
import random


dimX = dimY = 6

starterMap = np.zeros((dimX, dimY), dtype=int)
randRow = random.randint(1, dimX)
starterMap[randRow-1:randRow] = 1
starterMap[randRow-1][random.randint(0, dimY-1)] = 0


# randColum = random.randint(1, dimY)
# starterMap[:, randRow-1] = 1

print(repr(starterMap))



# array([[0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]])