import numpy as np
from numpy.linalg import norm

v = np.array([[1,2,3]])
v2 = np.array([[3,2,8]])

print(np.arccos(np.dot(v,v2.T)/(norm(v)*norm(v2))))
