import os
import time
import random
from CA import *



print("=============STATUS============")
print(" heh nothing here atm")
print("===========END STATUS==========")







m,n = 5000,5000
# m, n = os.get_terminal_size()
# n = n-2

sleep = 0
DISPLAY = False

# empty grid
# mat = [[0 for _ in range(m)] for _ in range(n)]


perc = 0.10 #amount of 1s
mat = [[True if random.random() < perc else False for _ in range(m)] for _ in range(n)]
# mat = [[random.random() for _ in range(m)] for _ in range(n)]

mat = np.array(mat)

#pong mat for GPU run
flip_mat = np.array([[True for _ in range(m)] for _ in range(n)])


iteration = 0
while True:
    print("step ", iteration)
    iteration+=1
    if DISPLAY: os.system("clear");print("q to quit; iteration : ", iteration);printMat(mat)
    # if input() == 'q': quit()
    time.sleep(sleep) # timing fpf


    step_GPU(mat, mask, flip_mat)


    #flip matrices
    mat,flip_mat = flip_mat, mat
    average = compute_percentage(mat)
    print("occupation: ",average)
    if average == 0.0 or average == 1.0: quit()



    




# 