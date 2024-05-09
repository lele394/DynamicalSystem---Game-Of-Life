import numpy as np



# uncomment fro game of life
mask = np.array([[1 ,    1  ,   1  ],
        [1   ,  9 ,  1    ],
        [1,     1  ,  1   ]])


# def activation(x):
#     # space ships
#     # return x*x

#     # return -1./pow(2., (0.6*pow(x, 2.)))+1.

#     # game of life
#     if x == 3. or x == 11. or x == 12. :
#         return 1
#     else:
#         return 0
    




def printMat(mat):
    print("===================================")
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
    print("===================================")




# def step(input, filter):
#     output = np.copy(input)

#     xSize, ySize = input.shape

#     for x in range(xSize):
#         for y in range(ySize):
#             sum = 0
#             for subx in [-1, 0, 1]:
#                 for suby in [-1, 0, 1]:
#                     sum += input[(subx + x) % xSize, (suby + y) % ySize] * filter[subx + 1, suby + 1]
#             sum = activation(sum)
#             # if sum < 0: # clamping
#             #     sum = 0
#             # elif sum > 1:
#             #     sum = 1
#             output[x, y] = sum
#     return output



import numba as nb

@nb.njit
def activation_GPU(x):
    # space ships
    # return x*x

    # return -1./pow(2., (0.6*pow(x, 2.)))+1.

    # game of life
    if x == 3. or x == 11. or x == 12. :
        return True
    else:
        return False

#space ship
# @nb.njit
# def activation_GPU(x):
#     # space ships
#     return x*x



@nb.njit(parallel=True)
def step_GPU(input, filter, output):
    xSize, ySize = input.shape
    for x in range(xSize):
        for y in range(ySize):
            s = 0
            for subx in [-1, 0, 1]:
                for suby in [-1, 0, 1]:
                    x_idx = (x + subx) % xSize
                    y_idx = (y + suby) % ySize
                    s += input[x_idx, y_idx] * filter[subx + 1, suby + 1]
            output[x, y] = activation_GPU(s)



@nb.njit(parallel=True)
def compute_percentage(mat):
    total_true_count = 0
    total_cell_count = 0
    for i in range(len(mat)):
        total_true_count += np.sum(mat[i])  # Count the number of True values in the subarray
        total_cell_count += len(mat[i])  # Count the total number of cells in the subarray
    return total_true_count / total_cell_count * 100  # Calculate the percentage
