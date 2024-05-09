"""
Lyapounov exponent using the tychonoff distance directly 

 - first set : Mo the original, non perturbated matrix.
               Mp the original, perturbated matrix         # YES
 - Compute the Tychonoff distance of Mo,Mp # YES
 - Run the simulation for n steps
 - Compute the new Tychonoff distance
 - plug into the Lyapounoff expression (limsup(1/N*ln(d(Mon, Mpn)/d(Mo, Mp))))


 Refactor to bundle in a function.


"""
import random
import numpy as np


perturbation_scale = 2000

simulation_steps = 300


size = 2000

perc = 0.5
m,n = size, size
Mo = np.array([[random.random() for _ in range(m)] for _ in range(n)])



def PullPerturbation(n_of_cells, dim):

    dim = dim-1 # python starts at 0

    # infinite loop escape check
    if n_of_cells>dim*dim: return "Too many perturbations asked for the dimension."

    # list of perturbations
    pert = []

    for i in range(n_of_cells):

        # to add the right number check
        added = False

        # no duplicate check
        while(not(added)):
            p = (random.randint(0, dim), random.randint(0, dim))
            if not( p in pert ):
                pert.append(p)
                added = True

    # print(pert)
    return pert





# gets a perturbation list
pert = PullPerturbation(perturbation_scale, len(Mo))



def applyPerturbation(perturbation_list, matrix):

    for perturbation in perturbation_list:
        # flip the cell
        matrix[perturbation[0], perturbation[1]] = (1+ matrix[perturbation[0]][perturbation[1]])%2

    return matrix


# copies the original matrix and applies a perturbation
Mp = np.copy(Mo)
applyPerturbation(pert, Mp)


# print(Mo == Mp)
# print(Mo)
# print(Mp)


import tools.Tychonoff as t


tychonoff_distance = t.sum_of_diff_GPU


# in a list because we will graph it.
lyapounov_list = []

first_tycho_dist = tychonoff_distance(Mo, Mp)
print("First distance : ", first_tycho_dist)






d_l = 50

import CA as ca
import math
# runs the simulation for a number of steps

# ca.printMat(Mo)
# ca.printMat(Mp)

# orginal
# for i in range(simulation_steps):
#     Mo = ca.step_GPU(Mo, ca.mask)
#     Mp = ca.step_GPU(Mp, ca.mask)

#GPU
for i in range(simulation_steps):
    ca.step_GPU(Mo, ca.ss_mask, Mo)
    ca.step_GPU(Mp, ca.ss_mask, Mp)



    # compute lyapounov exponent at that step
    # 1/N*ln(d(Mon, Mpn)/d(Mo, Mp))
    try:
        lyapounov_list.append(
            1/(i+1) * math.log(tychonoff_distance(Mo, Mp)/first_tycho_dist)
        )
    except ValueError as e:
        print(f' at {i}, Error computing Lyapounov exponent, following distance was computed ',
              tychonoff_distance(Mo, Mp), '                                            ')
        print(e)

    print('['+ 
          "".join(["#" for _ in range(math.floor(i/simulation_steps * d_l)) ])+">"+ 
          "".join(["-" for _ in range(d_l-math.floor(i/simulation_steps * d_l)-1) ])+  
          ']', f'  {math.floor(i/simulation_steps * 10000)/100}%   ',
          f'iteration {i}   last Lyapounov exponent {lyapounov_list[-1]}',
          end="\r")




import matplotlib.pyplot as plt
plt.plot(lyapounov_list)
plt.xlabel("n")
plt.ylabel("Lyapounov exponent")
plt.show()

