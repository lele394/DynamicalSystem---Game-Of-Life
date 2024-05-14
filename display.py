import json
import matplotlib.pyplot as plt

# Load JSON data
with open('run1_10_5000_0.025to0.075.json', 'r') as f:
    data1 = json.load(f)

with open('run1_10_1000_20_0to0.2.json', 'r') as f:
    data2 = json.load(f)

with open('run1_10_1000_20.json', 'r') as f:
    data3 = json.load(f)

with open('run1_0.045_10k.json', 'r') as f:
    plateau = json.load(f)



# =========== FINAL STABILITY PERCENTAGE ================

def average_final(data,label):

    # Initialize lists to store keys and averages
    keys = []
    averages = []
    # Iterate over each key-value pair in the data
    for key, values in data.items():

        averages.append(sum([values[i][-1] for i in range(len(values))])/len(values))
        keys.append(float(key))


    # Plot keys against averages
    plt.plot(keys, averages, label=label)
    plt.xlabel('Starting percentage')
    plt.ylabel('Average of Last Value')
    plt.title('Average of Last Value for Each Key')
    plt.grid(True)





def evolution(data,number):

    # Initialize lists to store keys and averages
    keys = []
    # averages = []
    # Iterate over each key-value pair in the data
    for key, values in data.items():

        # averages.append(sum([values[i][-1] for i in range(len(values))])/len(values))
        keys.append(key)


    # Plot keys against averages
    i = 0
    for line in data[keys[number]]:
        # plt.plot([float(keys[number])] + line, label=i)
        plt.plot([float(keys[number])] + line, label=i)
        i+=1
    plt.xlabel('Filling percentage')
    plt.title('Evolution of each run with starting percentage of '+ str(keys[number]))
    plt.grid(True)




def average_curve(curves):
    # Check if curves list is not empty
    if not curves:
        return None

    # Initialize the new curve with the same number of points as the first curve
    num_points = len(curves[0])
    new_curve = [0] * num_points

    # Calculate the average value for each point across all curves
    for curve in curves:
        for i, point in enumerate(curve):
            new_curve[i] += point

    # Divide each summed value by the number of curves to get the average
    new_curve = [value / len(curves) for value in new_curve]

    return new_curve

def evolution_average(data,number):

    # Initialize lists to store keys and averages
    keys = []
    # averages = []
    # Iterate over each key-value pair in the data
    for key, values in data.items():

        # averages.append(sum([values[i][-1] for i in range(len(values))])/len(values))
        keys.append(key)


    curve = average_curve(data[keys[number]])
    # Plot keys against averages
    plt.plot([float(keys[number])] + average_curve(data[keys[number]]), label="{:.3f}".format(float(keys[number])*100)+"%")
    # if i == 16:plt.plot( curve, label=i, color="red")
    # else: plt.plot( curve, label=i, color="black")
    plt.xlabel('Step')
    plt.ylabel('Filling percentage')
    plt.title('Evolution of each run')
    plt.grid(True)
    print(keys[number])

    return curve






def average_not_final(data,label, num):

    # Initialize lists to store keys and averages
    keys = []
    averages = []
    # Iterate over each key-value pair in the data
    for key, values in data.items():
        try:
            averages.append(sum([values[i][num] for i in range(len(values))])/len(values))
            keys.append(float(key))
        except:
            averages.append(0)
            keys.append(float(key))
            print(f'unavailable for {key}')

    return [keys, averages]












# code used in the first 2 graphs
# average_final(data3, "Full sweep")# used in the first graph
# average_final(data2, "0 to 0.2") 
# average_final(data1, "0.025 to 0.075")
# plt.title("Average of Last Value for Each Starting Filling Percentage")
# plt.xlim(0,0.3)# 2nd graph window
# plt.legend()
# plt.show()


# evolution(plateau, 0)
# plt.show()


#============================================
# for fig 3 and fig 4
# for i in range(10):
#     evolution_average(data3, i*2)

# plt.legend()
# plt.show()






# plots allllll the curves. Overloads the plot though
# for i in range(20):
#     evolution(data3, i)
#     plt.xlabel('Filling percentage')
#     # plt.title('Evolution of each run')
#     plt.ylim(0,1)
#     plt.xlim(0,1000)
# plt.show()







# #fitting to exponential
# import numpy as np
# def f(x, a, b, c):
#     return np.exp(-a*x+b)+c




# skip = 100
# y = evolution_average(data3, 8)[skip:]
# plt.show()
# x = [i+skip for i in range(len(y))]
# print(len(y))

# from scipy.optimize import curve_fit
# params, covariance = curve_fit(f, x, y, [0.001, 0.045, 0.045])

# print("Fitted parameters:", params)


# # Predicted y values using the fitted function
# y_fit = [f(i, *params) for i in x]

# # Plotting (optional)
# import matplotlib.pyplot as plt
# plt.plot(x, y, 'b+', label='Data')
# plt.plot(x, y_fit, 'r-', label='Fitted curve')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()





















curves = []
# test 3D representation of average evolution
for i in range(1000):
    curves += [
    average_not_final(data3, "Full sweep", i),# used in the first graph
    # average_not_final(data2, "0 to 0.2",i) ,
    # average_not_final(data1, "0.025 to 0.075",i)

    ]

print(len(curves[0][1]))

from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Initialize the plot objects (lines) for each curve
lines = [ax.plot([], [], marker='o')[0] for _ in [curves[0]]]

# Update function to animate the curves
def update(frame):
    ax.set_title(f'Cycle {frame}')
    for i, line in enumerate(lines):
        line.set_data(curves[frame][0], curves[frame][1])
    return lines

# Create the animation
ani = FuncAnimation(fig, update, frames=1000, interval=10)

# Show the animation
plt.show()

ani.save('animation.gif', writer='pillow', fps=10)


# quit()


