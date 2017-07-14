import numpy as np

h = np.random.random([10,10,10])
print(h)

minValue = h.min()
maxValue = h.max()
print(minValue,maxValue)