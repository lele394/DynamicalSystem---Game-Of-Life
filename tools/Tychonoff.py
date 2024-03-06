import math


class InvalidSize(Exception):
    def __init__(self,  message="Size not right, debug size and check again"):
        self.message = message
        super().__init__(self.message)

class InvalidRadius(Exception):
    def __init__(self,  message="Radii are not equal."):
        self.message = message
        super().__init__(self.message)


def Tychonoff_Distance(m1, m2):
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
                return r
            
        #on y bottom 
        for x in range(-r, r+1):
            if m1[off_x+x][off_y+-r] != m2[off_x+x][off_y+-r]:
                return r
            
        #side x minus
        for y in range(-r, r+1):
            if m1[off_x+-r][off_y+y] != m2[off_x+-r][off_y+y]:
                return r

        #side x positive
        for y in range(-r, r+1):
            if m1[off_x+r][off_y+y] != m2[off_x+r][off_y+y]:
                return r

    return "Matrices look identical"

