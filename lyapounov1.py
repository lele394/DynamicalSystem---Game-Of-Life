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


perturbation_scale = 2

perc = 0.5
m,n = 3,3
Mo = [[1 if random.random() < perc else 0 for _ in range(m)] for _ in range(n)]



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

    return pert





# gets a perturbation list
pert = PullPerturbation(perturbation_scale, len(Mo))



def applyPerturbation(perturbation_list, matrix):

    for perturbation in perturbation_list:
        # flip the cell
        matrix[perturbation[0]][perturbation[1]] = (1+ matrix[perturbation[0]][perturbation[1]])%2

    return matrix


# copies the original matrix and applies a perturbation
Mp = [list(i) for i in Mo]
applyPerturbation(pert, Mp)


# print(Mo == Mp)
# print(Mo)
# print(Mp)


import tools.Tychonoff as t

tycho_dist = t.Tychonoff_Distance(Mo, Mp)

print(tycho_dist)








