import os
import time
import random


m,n = 11,11
# m, n = os.get_terminal_size()
n = n-2

sleep = 0.5


# empty grid
# mat = [[0 for _ in range(m)] for _ in range(n)]


perc = 0.10 #amount of 1s
mat = [[1 if random.random() < perc else 0 for _ in range(m)] for _ in range(n)]
# mat = [[random.random() for _ in range(m)] for _ in range(n)]


# uncomment fro game of life
mask = [[1 ,    1  ,   1  ],
        [1   ,  9 ,  1    ],
        [1,     1  ,  1   ]]

# fancy space ships not working
# mask = [[-0.8300993, -0.44785473, 0.979766 ],
# [-0.47983372, 0.07656833, -0.35514032],
# [ 0.53823346, 0.43503127, 0.2492277 ]] 

def activation(x):
    # space ships
    # return x*x

    # return -1./pow(2., (0.6*pow(x, 2.)))+1.

    # game of life
    if x == 3. or x == 11. or x == 12. :
        return 1
    else:
        return 0


def printMat(mat):
    for row in mat:
        ln = ""
        for element in row:
            if element < 0.2:
                ln += ' '
            elif element < 0.4:
                ln += '░'
            elif element < 0.6:
                ln += '▒'
            elif element < 0.8:
                ln += '▓'
            else:
                ln += '█'
        print(ln)





def step(input, filter):

    output = input.copy()

    xSize = len(input)
    ySize = len(input[0])

    for x in range(xSize):
        for y in range(ySize):
            sum = 0
            for subx in [-1, 0, 1]:
                for suby in [-1, 0, 1]:
                    sum += input[(subx + x) % xSize][(suby + y) % ySize] * filter[subx + 1][suby + 1]
            sum = activation(sum)
            # if sum < 0: # clamping
            #     sum = 0
            # elif sum > 1:
            #     sum = 1
            output[x][y] = sum
    return output
    




iteration = 0
while True:
    print("q to quit; iteration : ", iteration)
    iteration+=1
    printMat(mat)
    # if input() == 'q': quit()
    time.sleep(sleep) # timing fpf
    os.system("clear")
    mat = step(mat, mask)




# 