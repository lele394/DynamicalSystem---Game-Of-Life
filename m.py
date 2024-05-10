import os
import time
import random
from CA import *


print("=============STATUS============")
print(" heh nothing here atm")
print("===========END STATUS==========")


json_path = "test.json"
# max available iteration per run
max_iteration = 1000
run_for_average = 10

# number of points in the sweep
sweep_points = 20
sweep = np.linspace(0.0, 1.0, sweep_points)




m,n = 500,500
# m, n = os.get_terminal_size()
# n = n-2

sleep = 0
DISPLAY = False

# empty grid
# mat = [[0 for _ in range(m)] for _ in range(n)]








average = 0
percs = {}
for perc in sweep:
    runs = []
    for run in range(run_for_average):
        print("occupation: ",average, " percentages: ", perc, "run: ", run)

        mat = [[True if random.random() < perc else False for _ in range(m)] for _ in range(n)]
        # mat = [[random.random() for _ in range(m)] for _ in range(n)]
        mat = np.array(mat)

        #pong mat for GPU run
        flip_mat = np.array([[True for _ in range(m)] for _ in range(n)])

        averages = []
        iteration = 0

        keep = True
        while keep and iteration < max_iteration:
            iteration+=1
            if DISPLAY: os.system("clear");print("q to quit; iteration : ", iteration);printMat(mat)
            # if input() == 'q': quit()
            time.sleep(sleep) # timing fpf

            step_GPU(mat, mask, flip_mat)

            #flip matrices
            mat,flip_mat = flip_mat, mat
            average = compute_percentage(mat)
            if average == 0.0 or average == 1.0: keep = False
            averages.append(average)
        runs.append(averages)

    percs[str(perc)] = runs

import saver
saver.save_to_json(json_path, percs)







# 