import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])

meanX = np.mean(x)
meanY = np.mean(y)

sum=np.sum((x-meanX)*(y-meanY))
sum2 = np.sum(np.square(x-meanX))
slope = np.divide(sum,sum2)
B0 = meanY-(slope*meanX)

eq = slope*x + B0
plt.scatter(x,y)
plt.plot(x,eq)
plt.show()
