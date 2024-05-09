import math


class InvalidSize(Exception):
    def __init__(self,  message="Size not right, debug size and check again"):
        self.message = message
        super().__init__(self.message)

class InvalidRadius(Exception):
    def __init__(self,  message="Radii are not equal."):
        self.message = message
        super().__init__(self.message)


def Circle_Tychonoff_Distance(m1, m2):
    """
    Returns the Tychonoff distance between M1 and M2
    Matrices sizes must be the same and odd
    Matrices must be square
    """

    # same size check/sq
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]) or len(m1) != len(m1[0]): raise InvalidSize

    # find middle offset
    off_x, off_y = ( math.floor(len(m1)/2), math.floor(len(m1[0])/2) )
    if off_x != off_y: raise InvalidRadius

    # max radii
    max_radius = off_x




    for r in range(max_radius+1):

        # print(r)

        #on y top
        for x in range(-r, r+1):
            if m1[off_x+x][off_y+r] != m2[off_x+x][off_y+r]:
                return r+1
            
        #on y bottom 
        for x in range(-r, r+1):
            if m1[off_x+x][off_y+-r] != m2[off_x+x][off_y+-r]:
                return r+1
            
        #side x minus
        for y in range(-r, r+1):
            if m1[off_x+-r][off_y+y] != m2[off_x+-r][off_y+y]:
                return r+1

        #side x positive
        for y in range(-r, r+1):
            if m1[off_x+r][off_y+y] != m2[off_x+r][off_y+y]:
                return r+1

    return "Matrices look identical"








def Linear_Tychonoff_Distance(m1, m2):
    """ Support whatever matrix as long as they are the same"""

    for x in range(len(m1)):
        for y in range(len(m1[0])):
            if m1[x][y] != m2[x][y]:
                return x+y
    







import numpy as np
def mask_comparison(m1, m2):
    return np.sum(m1 != m2)


import numba as nb

@nb.njit(parallel=True)
def mask_comparison_GPU(grid1, grid2):
    differences = 0
    for i in nb.prange(grid1.shape[0]):
        for j in range(grid1.shape[1]):
            if grid1[i, j] != grid2[i, j]:
                differences += 1
    return differences


def sum_of_diff_GPU(array1, array2):
    print(array1)
    result = 0
    for i in range(array1.shape[0]):
        for j in range(array1.shape[1]):
            result += np.abs(array1[i, j] - array2[i, j])
    return result








