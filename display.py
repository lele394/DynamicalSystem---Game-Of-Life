import json
import matplotlib.pyplot as plt

# Load JSON data
with open('test.json', 'r') as f:
    data = json.load(f)




# =========== FINAL STABILITY PERCENTAGE ================

# Initialize lists to store keys and averages
keys = []
averages = []

# Iterate over each key-value pair in the data
for key, values in data.items():

    averages.append(sum([values[i][-1] for i in range(len(values))])/len(values))
    keys.append(float(key))


# Plot keys against averages
plt.plot(keys, averages)
plt.xlabel('Key')
plt.ylabel('Average of Last Value')
plt.title('Average of Last Value for Each Key')
plt.grid(True)
plt.show()
