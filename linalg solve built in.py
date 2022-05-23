import numpy as np
import numpy.linalg


a = np.array([[8,3,-3],[-2,-8,5],[3,5,10]])

b = np.array([[14],[5],[-8]])

print(np.linalg.solve(a,b))